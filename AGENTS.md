# Regras permanentes do projeto

## Objetivo

Este repositório mantém o curso preparatório premium para o concurso SAPE/SC. Toda contribuição deve priorizar correção, clareza didática, rastreabilidade e geração multiformato.

## Escopo e fonte canônica

- Markdown em `docs/` é a fonte canônica do material publicável.
- `questoes/`, `flashcards/`, `simulados/` e `assets/` permanecem separados enquanto a arquitetura definitiva desses dados não for aprovada.
- Não duplicar manualmente conteúdo para site, PDF e Word.
- Não mover nem renomear a estrutura existente sem autorização expressa.
- Não criar aulas, questões, flashcards ou simulados sem solicitação expressa.

## Regras editoriais

- Seguir integralmente `STYLE_GUIDE.md`.
- Usar português brasileiro, codificação UTF-8, linguagem objetiva e tom profissional.
- Não inventar leis, referências, jurisprudência, estatísticas, dados do edital ou entendimentos de banca.
- Toda afirmação normativa ou temporal deve indicar fonte oficial e data de consulta durante a futura produção didática.
- Não reproduzir material protegido de terceiros sem autorização ou base jurídica documentada.
- Não incluir dados pessoais, credenciais, segredos ou informações sigilosas.
- Manter links, títulos e referências internas válidos.

## Fluxo de trabalho

- Antes de editar, ler `README.md`, `CONTRIBUTING.md`, `STYLE_GUIDE.md` e os arquivos locais relacionados à tarefa.
- Preservar mudanças existentes do usuário e limitar o diff ao escopo solicitado.
- Preferir alterações pequenas, verificáveis e reversíveis.
- Não fazer commit, push, merge, release ou deploy sem autorização expressa.
- Não reescrever o histórico Git nem executar operações destrutivas.
- Não adicionar dependências sem justificar finalidade, manutenção e impacto no build.
- Arquivos gerados (`site/`, `build/`, PDF, DOCX e pacotes) não devem ser versionados.

## Critérios mínimos de qualidade

- O site deve compilar com `mkdocs build --strict` quando as dependências estiverem instaladas.
- Markdown deve respeitar hierarquia de títulos, links relativos e acessibilidade.
- Arquivos YAML devem ser válidos e usar dois espaços de indentação.
- Imagens futuras devem ter texto alternativo, origem e licença registradas.
- Mudanças editoriais futuras devem passar por revisão técnica, pedagógica, linguística e de fontes.
- Conteúdo publicado não pode conter `TODO`, `TBD`, marcadores vazios ou referências quebradas.

## Definição de pronto

Uma alteração está pronta quando cumpre o pedido, respeita o guia editorial, não introduz conteúdo especulativo, passa nas validações aplicáveis e tem seu impacto descrito claramente para revisão.
