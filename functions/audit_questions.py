"""Inventaria questões objetivas e calcula métricas verificáveis do curso."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEARCH_ROOTS = (
    ROOT / "docs" / "01-portugues",
    ROOT / "docs" / "03-administracao-geral",
    ROOT / "questoes" / "administracao-geral",
)
DETAIL = re.compile(r'^\?\?\?\s+\w+\s+"[^"]+"', re.MULTILINE)
HEADING = re.compile(r"^#{2,6}\s+", re.MULTILINE)
OPTION = re.compile(
    r"(?:^|(?<=\s))([A-E])[.)]\s+(.*?)(?=(?:\s+[A-E][.)]\s+)|\n|$)",
    re.MULTILINE,
)
ANSWER_PATTERNS = (
    re.compile(r"\*\*Resposta:\*\*\s*([A-E])\b", re.IGNORECASE),
    re.compile(r"\*\*Resposta:\s*([A-E])[.:]?\*\*", re.IGNORECASE),
    re.compile(r"^\s{4}\*\*([A-E])[.:]\*\*", re.MULTILINE),
    re.compile(r"^\s{4}\*\*([A-E])\.\*\*", re.MULTILINE),
    re.compile(r"^\s{4}\*\*([A-E])\*\*(?:\s|[,.:])", re.MULTILINE),
)
COMPACT = re.compile(r"^\*\*(\d+)\.\*\*\s+(.*)$", re.MULTILINE)


def discipline(path: Path) -> str:
    return "Língua Portuguesa" if "01-portugues" in path.parts else "Administração Geral"


def module(path: Path) -> str:
    match = re.search(r"modulo-(\d+)", str(path))
    if not match and "03-administracao-geral" in path.parts and re.match(r"0[1-5]-", path.name):
        return "Módulo 1"
    return f"Módulo {int(match.group(1))}" if match else "Sem módulo"


def alternatives(text: str) -> dict[str, str]:
    return {letter: re.sub(r"\s+", " ", value).strip() for letter, value in OPTION.findall(text)}


def answer(text: str) -> str | None:
    for pattern in ANSWER_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(1).upper()
    return None


def is_strictly_longest(lengths: dict[str, int], key: str) -> bool:
    correct = lengths.get(key)
    return correct is not None and all(correct > size for letter, size in lengths.items() if letter != key)


def previous_boundary(text: str, position: int) -> int:
    candidates = [0]
    candidates.extend(match.end() for match in HEADING.finditer(text, 0, position))
    candidates.extend(match.end() for match in DETAIL.finditer(text, 0, position))
    return max(candidates)


def next_boundary(text: str, position: int) -> int:
    candidates = [len(text)]
    heading = HEADING.search(text, position)
    detail = DETAIL.search(text, position)
    if heading:
        candidates.append(heading.start())
    if detail:
        candidates.append(detail.start())
    return min(candidates)


def individual_records(path: Path, text: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for index, detail in enumerate(DETAIL.finditer(text), start=1):
        before = text[previous_boundary(text, detail.start()) : detail.start()]
        opts = alternatives(before)
        if len(opts) < 2:
            continue
        after = text[detail.end() : next_boundary(text, detail.end())]
        key = answer(after)
        if not key:
            continue
        lengths = {letter: len(value) for letter, value in opts.items()}
        records.append(
            {
                "id": f"{path.relative_to(ROOT).as_posix()}::individual-{index}",
                "file": path.relative_to(ROOT).as_posix(),
                "discipline": discipline(path),
                "module": module(path),
                "format": "individual",
                "answer": key,
                "alternatives": opts,
                "lengths": lengths,
                "correct_is_longest": is_strictly_longest(lengths, key),
            }
        )
    return records


def compact_records(path: Path, text: str) -> list[dict[str, object]]:
    if "simulado" not in path.name:
        return []
    tables = list(re.finditer(
        r"\|\s*Questão\s*\|([^\n]+)\n\s*\|[^\n]+\n\s*\|\s*Resposta\s*\|([^\n]+)",
        text,
        re.IGNORECASE,
    ))
    table = next((item for item in reversed(tables) if re.search(r"\b[A-E]\b", item.group(2))), None)
    if table is None:
        return []
    numbers = re.findall(r"\d+", table.group(1))
    keys = re.findall(r"\b[A-E]\b", table.group(2).upper())
    key_map = dict(zip(numbers, keys))
    matches = list(COMPACT.finditer(text))
    records: list[dict[str, object]] = []
    for index, match in enumerate(matches):
        number = match.group(1)
        if number not in key_map:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.start() : end]
        opts = alternatives(body)
        if len(opts) < 2:
            continue
        key = key_map[number]
        lengths = {letter: len(value) for letter, value in opts.items()}
        records.append(
            {
                "id": f"{path.relative_to(ROOT).as_posix()}::compact-{number}",
                "file": path.relative_to(ROOT).as_posix(),
                "discipline": discipline(path),
                "module": module(path),
                "format": "compact",
                "answer": key,
                "alternatives": opts,
                "lengths": lengths,
                "correct_is_longest": is_strictly_longest(lengths, key),
            }
        )
    return records


def collective_records(path: Path, text: str) -> list[dict[str, object]]:
    marker = re.search(
        r'^(?:## Gabarito comentado|\?\?\? success "Mostrar gabarito comentado")\s*$',
        text,
        re.MULTILINE,
    )
    if marker is None:
        return []
    answer_map = {
        number: key
        for number, key in re.findall(
            r"^\s*(\d+)\.\s+\*\*([A-E])\.", text[marker.end() :], re.MULTILINE
        )
    }
    headings = list(re.finditer(r"^### Questão (\d+)\s*$", text[: marker.start()], re.MULTILINE))
    records: list[dict[str, object]] = []
    for index, heading in enumerate(headings):
        number = heading.group(1)
        key = answer_map.get(number)
        if key is None:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else marker.start()
        opts = alternatives(text[heading.end() : end])
        if len(opts) < 2:
            continue
        lengths = {letter: len(value) for letter, value in opts.items()}
        records.append(
            {
                "id": f"{path.relative_to(ROOT).as_posix()}::collective-{number}",
                "file": path.relative_to(ROOT).as_posix(),
                "discipline": discipline(path),
                "module": module(path),
                "format": "collective",
                "answer": key,
                "alternatives": opts,
                "lengths": lengths,
                "correct_is_longest": is_strictly_longest(lengths, key),
            }
        )
    return records


def hybrid_exercise_records(path: Path, text: str) -> list[dict[str, object]]:
    """Lê os itens objetivos curtos misturados a perguntas abertas de fixação."""
    records: list[dict[str, object]] = []
    headings = list(re.finditer(r"^### (\d+)\. .+$", text, re.MULTILINE))
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[heading.end() : end]
        opts = alternatives(body)
        if len(opts) < 2:
            continue
        number = heading.group(1)
        response = re.search(
            rf'^\s{{4}}\*\*{number}\. ([A-E])\.\*\*', text[end:], re.MULTILINE
        )
        if response is None:
            continue
        key = response.group(1)
        lengths = {letter: len(value) for letter, value in opts.items()}
        records.append(
            {
                "id": f"{path.relative_to(ROOT).as_posix()}::hybrid-{number}",
                "file": path.relative_to(ROOT).as_posix(),
                "discipline": discipline(path),
                "module": module(path),
                "format": "hybrid",
                "answer": key,
                "alternatives": opts,
                "lengths": lengths,
                "correct_is_longest": is_strictly_longest(lengths, key),
            }
        )
    return records


def summarize(records: list[dict[str, object]]) -> dict[str, object]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    groups["Curso inteiro"] = records
    for record in records:
        groups[str(record["discipline"])].append(record)
        groups[f'{record["discipline"]} — {record["module"]}'].append(record)
        groups[str(record["file"])].append(record)
    result: dict[str, object] = {}
    for name, items in groups.items():
        distribution = Counter(str(item["answer"]) for item in items)
        longest = sum(bool(item["correct_is_longest"]) for item in items)
        result[name] = {
            "questions": len(items),
            "answers": {letter: distribution.get(letter, 0) for letter in "ABCDE"},
            "correct_longest": longest,
            "correct_longest_percent": round(100 * longest / len(items), 2) if items else 0,
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--records", action="store_true")
    parser.add_argument("--baseline", action="store_true", help="Lê o conteúdo versionado em HEAD.")
    args = parser.parse_args()
    records: list[dict[str, object]] = []
    for root in SEARCH_ROOTS:
        for path in sorted(root.rglob("*.md")):
            if "flashcard" in path.name:
                continue
            if args.baseline:
                relative = path.relative_to(ROOT).as_posix()
                completed = subprocess.run(
                    ["git", "show", f"HEAD:{relative}"],
                    cwd=ROOT,
                    check=True,
                    capture_output=True,
                )
                text = completed.stdout.decode("utf-8").replace("\r\n", "\n")
            else:
                text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
            records.extend(individual_records(path, text))
            records.extend(compact_records(path, text))
            records.extend(collective_records(path, text))
            records.extend(hybrid_exercise_records(path, text))
    payload = {"summary": summarize(records)}
    if args.records:
        payload["records"] = records
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
