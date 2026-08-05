"""Audita a estrutura publicável das aulas de Língua Portuguesa."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
LESSONS = sorted((ROOT / "docs" / "01-portugues").glob("modulo-*-aula-*.md"))
REQUIRED = (
    "id",
    "title",
    "description",
    "discipline",
    "module",
    "lesson",
    "status",
    "edital_refs",
    "prerequisites",
    "estimated_minutes",
    "authors",
    "reviewers",
    "last_reviewed",
    "sources",
    "tags",
)


def audit(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    errors: list[str] = []
    if raw.startswith(b"\xef\xbb\xbf"):
        errors.append("bom")
    try:
        text = raw.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError as exc:
        return {"file": path.name, "errors": [f"utf8: {exc}"]}

    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    metadata: dict[str, object] = {}
    if not match:
        errors.append("front-matter ausente, deslocado ou mal delimitado")
        body = text
    else:
        body = text[match.end() :]
        try:
            loaded = yaml.safe_load(match.group(1))
            if not isinstance(loaded, dict):
                errors.append("front-matter não é um mapa YAML")
            else:
                metadata = loaded
        except yaml.YAMLError as exc:
            errors.append(f"yaml: {str(exc).splitlines()[0]}")

    missing = [field for field in REQUIRED if field not in metadata]
    if missing:
        errors.append("campos ausentes: " + ", ".join(missing))

    h1 = len(re.findall(r"^# [^#]", body, re.MULTILINE))
    if h1 != 1:
        errors.append(f"títulos H1: {h1}")

    question_headings = len(re.findall(r"^#{2,3} Questão \d+", body, re.MULTILINE))
    compact_questions = len(re.findall(r"^\*\*\d+\.\*\*", body, re.MULTILINE))
    questions = max(question_headings, compact_questions)
    if questions < 10:
        errors.append(f"questões: {questions}")

    flashcard_section = re.search(
        r"^## Flashcards.*?(?=^## |\Z)", body, re.MULTILINE | re.DOTALL
    )
    flashcards = 0
    if flashcard_section:
        flashcards = len(
            re.findall(
                r'^\?\?\? question "Mostrar resposta"',
                flashcard_section.group(),
                re.MULTILINE,
            )
        )
    if flashcards < 10 or flashcards > 15:
        errors.append(f"flashcards: {flashcards}")

    details = len(re.findall(r'^\?\?\? question "', body, re.MULTILINE))
    raw_html = re.findall(r"<(section|div|span|strong)\b", body)
    ids = re.findall(r'\bid=["\']([^"\']+)', body)
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    if duplicate_ids:
        errors.append("ids duplicados: " + ", ".join(duplicate_ids))

    return {
        "file": path.name,
        "module": metadata.get("module"),
        "lesson": metadata.get("lesson"),
        "questions": questions,
        "flashcards": flashcards,
        "details": details,
        "html_tags": len(raw_html),
        "errors": errors,
    }


def main() -> int:
    results = [audit(path) for path in LESSONS]
    totals = {
        "lessons": len(results),
        "questions": sum(int(item.get("questions", 0)) for item in results),
        "flashcards": sum(int(item.get("flashcards", 0)) for item in results),
        "lessons_with_errors": sum(bool(item["errors"]) for item in results),
    }
    print(json.dumps({"totals": totals, "lessons": results}, ensure_ascii=False, indent=2))
    return 1 if totals["lessons_with_errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
