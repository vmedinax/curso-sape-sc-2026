# Auditoria técnica do projeto — Curso SAPE/SC 2026

**Data da auditoria:** 3 de agosto de 2026  
**Escopo:** estrutura local, arquivos rastreados, estado do Git, histórico disponível e arquitetura recomendada.  
**Restrição observada:** nenhum conteúdo didático foi criado e nenhum arquivo preexistente foi alterado. Este relatório é o único arquivo adicionado.

## 1. Resumo executivo

O repositório está em uma fase de **esqueleto inicial**. Há uma separação preliminar entre material teórico (`docs`), questões, simulados, flashcards e recursos visuais, mas ainda não existe uma plataforma de curso funcional nem uma convenção editorial formalizada.

No estado atual:

- existem 7 arquivos Markdown rastreados, todos com 0 bytes;
- existem 5 diretórios de primeiro nível e 12 diretórios temáticos dentro de `docs`, todos vazios;
- diretórios vazios não são rastreados pelo Git e, portanto, não fazem parte de um clone novo;
- não há configuração de GitHub Pages, gerador de site, automação, testes, licença, metadados, política editorial ou pipeline de PDF/Word;
- as branches locais `main` e `develop` apontam para o mesmo commit e acompanham as respectivas branches remotas;
- a árvore de trabalho estava limpa antes da criação deste relatório;
- o histórico tem somente 3 commits e precisa de saneamento de processo, embora não seja recomendável reescrevê-lo agora.

**Conclusão:** a taxonomia inicial é aproveitável, mas o projeto ainda não tem os mecanismos necessários para garantir consistência, rastreabilidade, publicação e geração multiformato. A prioridade deve ser criar a fundação editorial e técnica antes de produzir as aulas.

## 2. Inventário do estado atual

### 2.1 Estrutura encontrada

```text
curso-sape-sc-2026/
├── assets/                              (vazio)
├── docs/
│   ├── 00-guia-do-candidato/            (vazio)
│   ├── 01-portugues/                    (vazio)
│   ├── 02-raciocinio-logico/            (vazio)
│   ├── 03-administracao-geral/          (vazio)
│   ├── 04-administracao-publica/        (vazio)
│   ├── 05-direito-constitucional/       (vazio)
│   ├── 06-direito-administrativo/       (vazio)
│   ├── 07-afo/                          (vazio)
│   ├── 08-licitacoes/                   (vazio)
│   ├── 09-informatica/                  (vazio)
│   ├── 10-legislacao/                   (vazio)
│   ├── 11-conhecimentos-especificos/    (vazio)
│   └── INDEX.md                         (0 bytes)
├── flashcards/                          (vazio)
├── questoes/                            (vazio)
├── simulados/                           (vazio)
├── CHANGELOG.md                         (0 bytes)
├── CONTRIBUTING.md                      (0 bytes)
├── EDITAL.md                            (0 bytes)
├── PLANO_DE_ESTUDOS.md                  (0 bytes)
├── README.md                            (0 bytes)
└── ROADMAP.md                           (0 bytes)
```

### 2.2 Estado do Git

- Branch ativa: `develop`.
- `develop` acompanha `origin/develop` sem divergência detectada.
- `main` acompanha `origin/main`; ambas apontam para o mesmo commit da branch ativa.
- Branch padrão remota: `main`.
- Remote: repositório GitHub `vmedinax/curso-sape-sc-2026` via HTTPS.
- Nenhum arquivo `.gitignore`, `.gitattributes` ou `.editorconfig` foi encontrado.
- Nenhum arquivo de CI/CD ou configuração em `.github/` foi encontrado.

### 2.3 Observações sobre o histórico

O histórico contém três commits:

1. criação de um `README.md` com 19 linhas e uma lista inicial de disciplinas;
2. inclusão de um arquivo binário ZIP de 42.732 bytes;
3. criação do esqueleto atual, com remoção das 19 linhas do README e substituição/remoção prática do ZIP.

O ZIP não está na árvore atual, mas continua recuperável no histórico Git. Isso não representa um problema operacional imediato por ser pequeno, porém binários gerados não devem ser versionados no futuro. PDFs, DOCX e pacotes devem ser publicados como artefatos de workflow ou anexos de release.

## 3. Avaliação da organização

### 3.1 Pontos positivos

- A numeração das disciplinas fornece ordem estável para navegação.
- A separação de teoria, questões, flashcards e simulados reconhece tipos diferentes de material.
- Markdown é uma boa fonte canônica por ser legível, versionável e conversível.
- O uso de `main` e `develop` indica intenção de separar publicação e trabalho em andamento.

### 3.2 Lacunas e riscos

| Área | Situação | Risco | Prioridade |
|---|---|---|---|
| Fonte canônica | Não definida | Duplicação e divergência entre site, PDF e Word | Crítica |
| Estrutura das aulas | Sem padrão de arquivos ou metadados | Conteúdo inconsistente e difícil de automatizar | Crítica |
| Edital | Arquivo vazio e sem matriz de rastreabilidade | Cobertura incompleta ou impossível de auditar | Crítica |
| Publicação | GitHub Pages não configurado | Processo manual e sujeito a erros | Alta |
| Qualidade | Sem lint, validação de links ou revisão | Links quebrados e estilo inconsistente | Alta |
| Direitos autorais | Sem política de fontes/licença | Exposição jurídica e uso inadequado de material | Alta |
| Acessibilidade | Sem critérios | Experiência inferior e documentos menos inclusivos | Alta |
| Assets | Diretório genérico e vazio | Nomes ambíguos, duplicação e arquivos pesados | Média |
| Questões | Sem schema para metadados, gabarito e origem | Banco não pesquisável e difícil de manter | Crítica |
| Versionamento | Estratégia de branches não documentada | Fluxo complexo ou releases inconsistentes | Média |
| Artefatos | Sem política para PDF/DOCX | Binários podem voltar ao Git | Alta |
| Segurança | Sem atualização automática ou permissões de workflows | Dependências desatualizadas e CI excessivamente permissiva | Média |

## 4. Arquitetura recomendada

Recomenda-se manter **Markdown como fonte única da verdade** e gerar site, PDF e DOCX a partir dele. A estrutura abaixo separa conteúdo publicável, dados estruturados, recursos compartilhados, templates e automação.

```text
curso-sape-sc-2026/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── correcao.yml
│   │   └── novo-conteudo.yml
│   ├── pull_request_template.md
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       ├── pages.yml
│       └── release-materials.yml
├── docs/                              # Tudo que compõe o site/curso
│   ├── index.md
│   ├── guia/
│   ├── disciplinas/
│   │   ├── 01-portugues/
│   │   │   ├── index.md
│   │   │   ├── modulo-01/
│   │   │   │   ├── index.md
│   │   │   │   ├── aula-01.md
│   │   │   │   └── revisao.md
│   │   │   └── referencias.md
│   │   └── ...
│   ├── questoes/                     # Páginas geradas ou curadas para o site
│   ├── simulados/
│   ├── revisoes/
│   ├── glossario.md
│   └── assets/
│       ├── images/
│       ├── diagrams/
│       ├── stylesheets/
│       └── javascripts/
├── data/                              # Dados não publicados diretamente
│   ├── edital.yml
│   ├── disciplinas.yml
│   ├── questoes/
│   ├── flashcards/
│   └── simulados/
├── templates/
│   ├── aula.md
│   ├── questao.yml
│   ├── simulado.yml
│   ├── flashcard.yml
│   ├── reference.docx
│   ├── pdf-template.tex
│   └── cover.md
├── scripts/
│   ├── build-site.*
│   ├── build-pdf.*
│   ├── build-docx.*
│   ├── validate-content.*
│   └── generate-navigation.*
├── tests/
│   ├── content/
│   └── fixtures/
├── build/                             # Gerado; ignorado pelo Git
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .markdownlint-cli2.yaml
├── .pre-commit-config.yaml            # Opcional, recomendado
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── EDITAL.md
├── LICENSE
├── PLANO_DE_ESTUDOS.md
├── PROJECT_REVIEW.md
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── STYLE_GUIDE.md
├── CHANGELOG.md
├── mkdocs.yml
├── pyproject.toml                     # Dependências/ferramentas fixadas
└── requirements.lock                  # Ou lock equivalente
```

### Decisões estruturais recomendadas

1. **Mover o `assets` raiz para `docs/assets`.** Assim, recursos usados no site permanecem próximos do conteúdo publicável. Arquivos exclusivos de exportação ficam em `templates`.
2. **Mover dados de flashcards, questões e simulados para `data`.** Os registros devem ser estruturados em YAML/JSON, enquanto páginas legíveis ou geradas permanecem em `docs`.
3. **Agrupar as disciplinas em `docs/disciplinas`.** Isso reduz a poluição da raiz de `docs` e facilita regras e navegação compartilhadas.
4. **Trocar `docs/INDEX.md` por `docs/index.md`.** O nome minúsculo é a convenção dos geradores estáticos e evita diferenças entre sistemas de arquivos sensíveis a maiúsculas.
5. **Preservar prefixos numéricos somente onde expressam ordem pedagógica.** Slugs devem ser estáveis, minúsculos, sem acentos e com hífens.
6. **Não usar arquivos vazios para conservar diretórios.** Adicionar `index.md`, um README de escopo ou criar a pasta somente quando houver conteúdo real.
7. **Manter arquivos gerados fora do controle de versão.** `build/`, `site/`, PDFs e DOCX devem ser ignorados e distribuídos via GitHub Actions/Releases.

## 5. Arquivos que deveriam existir

### 5.1 Fundação obrigatória

| Arquivo | Finalidade |
|---|---|
| `README.md` | Proposta do curso, público, status, como navegar e como contribuir |
| `LICENSE` | Termos de uso do código e/ou material; deve ser escolhido conscientemente |
| `CONTRIBUTING.md` | Fluxo editorial, branches, commits, revisão e critérios de aceite |
| `STYLE_GUIDE.md` | Voz, terminologia, estrutura de aula, citações e formatação |
| `EDITAL.md` | Identificação do edital e visão humana da matriz de cobertura |
| `data/edital.yml` | Matriz estruturada entre item do edital, disciplina, aula e status |
| `ROADMAP.md` | Fases, entregáveis, critérios de conclusão e dependências |
| `CHANGELOG.md` | Alterações por versão seguindo Keep a Changelog |
| `.gitignore` | Exclusão de ambiente, cache, site, PDF, DOCX e temporários |
| `.gitattributes` | Normalização de fim de linha e tratamento de binários |
| `.editorconfig` | Codificação UTF-8, indentação e fim de linha consistentes |
| `mkdocs.yml` | Tema, navegação, plugins e extensões do site |
| `pyproject.toml` e lock | Dependências reprodutíveis e configuração de ferramentas |

### 5.2 Governança e qualidade

| Arquivo | Finalidade |
|---|---|
| `.github/workflows/ci.yml` | Lint, validação, links e build em pull requests |
| `.github/workflows/pages.yml` | Deploy do site somente a partir da branch de publicação |
| `.github/workflows/release-materials.yml` | Geração de PDF/DOCX e anexação a releases |
| `.github/pull_request_template.md` | Checklist editorial, técnico e jurídico |
| `.github/ISSUE_TEMPLATE/*.yml` | Relatos padronizados de erro e lacuna de conteúdo |
| `.github/dependabot.yml` | Atualizações controladas de Actions e dependências |
| `.markdownlint-cli2.yaml` | Regras de consistência Markdown |
| `.pre-commit-config.yaml` | Validações locais antes do commit |
| `CODE_OF_CONDUCT.md` | Regras de convivência caso haja colaboração pública |
| `SECURITY.md` | Canal para vulnerabilidades, especialmente se houver recursos interativos |
| `CITATION.cff` | Forma padronizada de citar o projeto |

### 5.3 Templates e schemas editoriais

| Arquivo | Finalidade |
|---|---|
| `templates/aula.md` | Front matter e seções obrigatórias de cada aula |
| `templates/questao.yml` | Identificador, banca, ano, tema, resposta, justificativa e fonte |
| `templates/flashcard.yml` | Pergunta, resposta, tags, origem e revisão |
| `templates/simulado.yml` | Composição, tempo, regras e vínculo com gabarito |
| `schemas/*.json` | Validação automática dos dados estruturados |
| `templates/reference.docx` | Estilos corporativos do Word usados pelo Pandoc |
| `templates/pdf-template.tex` | Tipografia, margens, cabeçalhos e identidade do PDF |

## 6. Padrão editorial e metadados

Cada aula deve começar com front matter YAML padronizado. Os campos recomendados, sem preencher conteúdo agora, são:

```yaml
---
id: disciplina-modulo-aula
title: "Título"
discipline: slug-da-disciplina
module: 1
lesson: 1
status: draft
edital_refs: []
prerequisites: []
estimated_minutes: 0
authors: []
reviewers: []
last_reviewed: null
sources: []
tags: []
---
```

Estados editoriais sugeridos: `planned`, `draft`, `technical-review`, `pedagogical-review`, `legal-review`, `approved`, `published`, `needs-update`.

Todo item do edital deve possuir identificador estável e estar ligado a pelo menos uma unidade didática, questões de fixação e uma evidência de revisão. Essa matriz é o principal controle contra lacunas de cobertura.

## 7. GitHub Pages

### Solução recomendada: MkDocs Material + GitHub Actions

Essa combinação é adequada porque trabalha nativamente com Markdown, oferece navegação, busca, bom suporte a dispositivos móveis, admonitions, tabs, diagramas e customização sem exigir uma aplicação complexa.

Fluxo recomendado:

```text
Markdown + dados → validação em PR → merge em main → build MkDocs → GitHub Pages
```

Configuração sugerida:

- `docs/` como diretório-fonte;
- `mkdocs.yml` na raiz;
- tema Material com paleta acessível e modo claro/escuro;
- navegação explícita inicialmente; gerar a navegação somente quando a escala justificar;
- busca em português;
- URLs estáveis e sem extensão;
- links relativos e validação automática de links internos;
- deploy com a action oficial `actions/deploy-pages` e permissões mínimas;
- ambiente GitHub `github-pages` protegido;
- domínio próprio configurado apenas quando definido, via `docs/CNAME`;
- analytics somente com decisão explícita sobre privacidade e consentimento.

Não se recomenda manter a saída compilada em uma branch manual ou commitar o diretório `site/`. O workflow deve produzir e publicar o artefato.

### Navegação sugerida

```text
Início
├── Guia do candidato
├── Plano de estudos
├── Disciplinas
│   ├── Português
│   ├── Raciocínio lógico
│   └── ...
├── Questões
├── Revisões e flashcards
├── Simulados
├── Glossário
└── Atualizações
```

## 8. Geração futura de PDF e Word

### Estratégia recomendada: Pandoc como conversor comum

O mesmo conjunto de Markdown aprovado deve alimentar os dois formatos:

```text
Markdown aprovado
├── Pandoc + template LaTeX → PDF
└── Pandoc + reference.docx → DOCX
```

Recomendações:

- usar uma lista ordenada de arquivos por volume/disciplina, sem depender de glob implícito;
- aplicar filtros Pandoc para links, caixas de destaque, respostas e referências;
- usar `--resource-path` para resolver imagens de forma previsível;
- gerar sumário, numeração, metadados, capa, cabeçalho e rodapé automaticamente;
- manter estilos Word em `templates/reference.docx`, não aplicar formatação manual após a geração;
- usar um template LaTeX versionado e fontes com licença compatível para PDF;
- garantir textos alternativos e legendas para imagens e tabelas;
- incorporar versão, hash do commit e data de geração no documento;
- gerar por disciplina e também uma edição completa, quando o volume permitir;
- publicar arquivos como artefatos de CI em testes e como assets de GitHub Release em versões;
- executar builds em container ou ambiente fixado para reprodutibilidade;
- excluir `build/`, `*.pdf` e `*.docx` do Git, salvo templates deliberados.

Antes da adoção definitiva, deve ser feita uma prova técnica com equações, tabelas longas, imagens, notas, links, caracteres portugueses e quebras de página. Isso evita escolher uma cadeia de geração que funcione apenas para documentos simples.

## 9. Qualidade, testes e critérios de aceite

O pipeline de CI deve impedir publicação quando houver:

- Markdown fora do padrão;
- front matter ausente ou inválido;
- identificadores duplicados;
- referências a itens inexistentes do edital;
- links ou imagens internas quebrados;
- arquivos excessivamente grandes ou binários não autorizados;
- questões sem origem, resposta ou justificativa;
- páginas órfãs fora da navegação;
- falha no build do site, PDF ou DOCX;
- termos proibidos ou marcadores pendentes (`TODO`, `TBD`) em conteúdo aprovado.

Além da validação automatizada, cada módulo deve passar por revisão em quatro dimensões: correção técnica, didática, linguagem e conformidade de fontes/direitos autorais.

## 10. Estratégia de Git e releases

Para uma equipe pequena, recomenda-se simplificar para **trunk-based development**:

- `main` sempre publicável;
- branches curtas do tipo `content/...`, `fix/...` e `chore/...`;
- pull request obrigatório com CI e ao menos uma revisão para mudanças editoriais relevantes;
- tags semânticas ou por edição, por exemplo `v1.0.0` ou `2026.08`;
- GitHub Releases contendo PDF/DOCX gerados e notas derivadas do changelog.

Se `develop` for mantida, sua função precisa ser documentada e o Pages deve publicar exclusivamente de `main`. No estágio atual, duas branches permanentes adicionam mais processo do que segurança.

Commits devem ser pequenos e descritivos. Binários gerados, exportações e arquivos compactados não devem ser incluídos. Não há necessidade de reescrever o histórico atual, salvo se o ZIP antigo contiver informação sensível ou material sem autorização — caso em que uma auditoria específica e remoção do histórico seriam necessárias.

## 11. Plano para profissionalização

### Fase 0 — Decisões de produto e conformidade

- Confirmar cargo(s), edital-base, banca, cronograma e público-alvo.
- Definir licença, política de acesso e limites entre material aberto e premium.
- Definir identidade visual, autoria, revisão e regras de uso de questões de terceiros.
- Critério de saída: decisões registradas e responsáveis definidos.

### Fase 1 — Fundação do repositório

- Criar arquivos de governança, padrões, templates, schemas e ignore rules.
- Reorganizar diretórios conforme a arquitetura proposta.
- Definir fonte canônica, IDs, slugs e estados editoriais.
- Simplificar/documentar o fluxo Git.
- Critério de saída: um clone novo reproduz estrutura e validações sem arquivos locais implícitos.

### Fase 2 — Plataforma e automação

- Configurar MkDocs Material e ambiente reprodutível.
- Implementar CI para Markdown, schemas, links e build.
- Implementar preview de pull requests quando viável.
- Configurar deploy protegido no GitHub Pages.
- Critério de saída: uma página estrutural de teste é validada e publicada automaticamente.

### Fase 3 — Pipeline editorial

- Transformar o edital em matriz rastreável.
- Definir modelo de aula, questão, flashcard, revisão e simulado.
- Estabelecer checklists e papéis de revisão.
- Criar painel de cobertura a partir dos dados.
- Critério de saída: um módulo-piloto estrutural atravessa todo o fluxo sem depender de operações manuais ocultas.

### Fase 4 — Exportação multiformato

- Configurar Pandoc, template PDF e referência DOCX.
- Testar elementos complexos e acessibilidade.
- Publicar artefatos versionados por release.
- Critério de saída: HTML, PDF e DOCX são produzidos da mesma fonte sem divergência material.

### Fase 5 — Produção e controle de qualidade

- Produzir por prioridade do edital e incidência, sem perder a matriz de cobertura.
- Revisar tecnicamente, pedagogicamente e juridicamente.
- Medir cobertura, defeitos, atualizações e desempenho editorial.
- Critério de saída: 100% dos itens planejados possuem estado, responsável, evidência e rastreabilidade.

### Fase 6 — Operação contínua

- Versionar atualizações legislativas e erratas.
- Automatizar verificação periódica de links e dependências.
- Manter changelog e releases reproduzíveis.
- Coletar feedback sem armazenar dados pessoais desnecessários.
- Critério de saída: processo de atualização testado, documentado e sustentável.

## 12. Prioridades imediatas

Ordem sugerida para a próxima intervenção:

1. decidir licença, modelo de acesso e edital oficial de referência;
2. aprovar a arquitetura e a estratégia de branches;
3. criar arquivos básicos de configuração e governança;
4. reorganizar o esqueleto sem escrever conteúdo didático;
5. configurar MkDocs e CI;
6. criar schemas e templates editoriais;
7. validar um fluxo estrutural de ponta a ponta;
8. somente então iniciar a produção do curso.

## 13. Itens que não devem ser feitos ainda

- Não começar aulas antes de fechar edital, metadados e template.
- Não copiar questões, textos legais comentados ou materiais de terceiros sem política de fonte e direitos.
- Não gerar e commitar PDF, DOCX ou ZIP.
- Não automatizar navegação a partir de convenções ainda instáveis.
- Não adicionar plugins sem fixar versões e justificar sua função.
- Não reescrever o histórico Git sem necessidade de segurança ou conformidade.

## 14. Resultado da auditoria

O projeto tem uma intenção estrutural correta, porém ainda não constitui um curso publicável. A melhor evolução é tratá-lo como um **sistema editorial versionado**, no qual Markdown e dados estruturados são a origem, GitHub Actions garante qualidade, MkDocs Material publica a experiência web e Pandoc gera PDF/DOCX reproduzíveis. A profissionalização depende primeiro da matriz do edital, das regras editoriais e da automação; o conteúdo deve vir depois dessa fundação.

