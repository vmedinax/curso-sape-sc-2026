# Curso Preparatório SAPE/SC 2026

Repositório editorial do curso preparatório premium para o concurso SAPE/SC. O projeto está em fase de fundação: a arquitetura, os padrões editoriais e a plataforma de publicação estão sendo preparados antes da produção das aulas.

## Estado do projeto

**Em estruturação.** Ainda não há conteúdo didático, banco de questões, flashcards ou simulados publicados. O edital-base, a licença do material e o fluxo de distribuição premium ainda precisam de decisão formal.

Consulte:

- [auditoria técnica](PROJECT_REVIEW.md);
- [roadmap](ROADMAP.md);
- [guia editorial](STYLE_GUIDE.md);
- [orientações para contribuição](CONTRIBUTING.md).

## Estrutura atual

```text
docs/          site e futuras unidades do curso
assets/        recursos compartilhados (reservado)
flashcards/    flashcards futuros (reservado)
questoes/      banco de questões futuro (reservado)
simulados/     simulados futuros (reservado)
```

As pastas numeradas em `docs/` definem a navegação inicial. A presença de uma disciplina na estrutura não confirma sua inclusão definitiva no edital; a matriz oficial será validada antes da produção.

## Site local

O site usa [MkDocs](https://www.mkdocs.org/) com o tema [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Com Python e a dependência `mkdocs-material` instalados:

```powershell
mkdocs serve
```

Para validar uma compilação estrita:

```powershell
mkdocs build --strict
```

As dependências ainda serão fixadas em uma etapa futura do roadmap. Não versione o diretório `site/` gerado pelo build.

## Como contribuir

Leia `AGENTS.md`, `CONTRIBUTING.md` e `STYLE_GUIDE.md` antes de propor alterações. Mudanças devem ser pequenas, rastreáveis e revisadas. Não inclua material de terceiros sem origem e permissão documentadas.

## Publicação e formatos

Markdown será a fonte canônica. O site será preparado para GitHub Pages; PDF e Word serão gerados futuramente a partir da mesma fonte, sem manter exportações no Git.

## Licença

A licença e os termos de acesso ainda não foram definidos. Até essa decisão, nenhum direito de reutilização ou redistribuição é concedido além do permitido pela legislação aplicável.
