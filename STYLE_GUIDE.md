# Guia de estilo editorial

Este documento define o padrão das futuras aulas do curso SAPE/SC. Ele estabelece estrutura e critérios, mas não autoriza a criação de conteúdo didático.

## Princípios

O material deve ser correto, direto, progressivo, rastreável e orientado ao edital. Clareza prevalece sobre ornamentação. Cada explicação deve ajudar o estudante a compreender, recordar ou aplicar um ponto claramente identificado.

## Idioma e tom

- Escrever em português brasileiro conforme a norma-padrão vigente.
- Usar tom profissional, acolhedor e seguro, sem promessas de aprovação.
- Preferir voz ativa, frases curtas e verbos concretos.
- Explicar siglas na primeira ocorrência.
- Evitar jargão desnecessário, humor que envelheça rapidamente e linguagem depreciativa.
- Tratar o leitor por “você” somente quando a orientação direta melhorar a compreensão.

## Estrutura obrigatória de uma aula

Cada futura aula deverá conter, nesta ordem:

1. front matter YAML;
2. título único de nível 1;
3. objetivos de aprendizagem verificáveis;
4. vínculo com os itens do edital;
5. pré-requisitos, quando existirem;
6. desenvolvimento organizado em seções progressivas;
7. exemplos autorais ou devidamente licenciados;
8. pontos de atenção e distinções relevantes;
9. resumo para revisão;
10. referências e data da última revisão.

Questões, flashcards e simulados obedecerão a modelos próprios quando forem aprovados. Eles não devem ser embutidos de forma improvisada nas aulas.

## Metadados

O front matter mínimo das futuras aulas será:

```yaml
---
id: disciplina-modulo-aula
title: "Título da aula"
discipline: slug-da-disciplina
module: 1
lesson: 1
status: planned
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

Regras dos campos:

- `id`: único, estável, minúsculo, sem acentos e separado por hífens;
- `title`: título humano e específico;
- `discipline`: igual ao slug da pasta;
- `module` e `lesson`: números inteiros positivos;
- `status`: um de `planned`, `draft`, `technical-review`, `pedagogical-review`, `legal-review`, `approved`, `published` ou `needs-update`;
- `edital_refs`: identificadores exatos da futura matriz do edital;
- `estimated_minutes`: estimativa realista de estudo;
- `sources`: identificadores ou referências completas e verificáveis;
- `last_reviewed`: data ISO `AAAA-MM-DD` após revisão efetiva.

## Hierarquia e formatação

- Usar um único `#` por página.
- Não saltar níveis de título.
- Títulos não levam ponto final e devem usar maiúsculas apenas onde a língua exigir.
- Preferir parágrafos curtos; usar listas quando houver itens realmente paralelos.
- Usar negrito com moderação e nunca como substituto de título.
- Reservar itálico para termos, obras e ênfase pontual.
- Usar crase para código, comandos, caminhos, campos e valores literais.
- Não usar HTML quando houver equivalente claro em Markdown.
- Tabelas devem ter cabeçalhos objetivos e permanecer legíveis em telas estreitas.

## Elementos didáticos

Admonitions do MkDocs devem ter função consistente:

- `note`: informação complementar;
- `tip`: estratégia prática de estudo ou resolução;
- `warning`: confusão frequente ou condição relevante;
- `danger`: erro grave capaz de invalidar uma resposta;
- `example`: aplicação ilustrativa.

Não acumular caixas de destaque. Uma informação central deve permanecer no fluxo principal do texto.

## Terminologia e precisão

- Criar e seguir um glossário para termos recorrentes.
- Distinguir regra, exceção, controvérsia e orientação de prova.
- Informar quando uma interpretação não for pacífica.
- Não apresentar inferência como texto legal ou entendimento oficial.
- Registrar datas de corte para normas e informações sujeitas a atualização.

## Fontes, citações e direitos autorais

- Priorizar fontes oficiais, legislação consolidada e documentos primários.
- Informar título, órgão ou autor, endereço e data de acesso quando aplicável.
- Citações literais devem ser curtas, necessárias e claramente atribuídas.
- Parafrasear não elimina a obrigação de citar a fonte.
- Questões de terceiros exigem registro de origem e análise de permissões de uso.
- Imagens, fontes e diagramas devem ter licença compatível documentada.

## Links e recursos visuais

- Usar links relativos para arquivos internos.
- O texto do link deve descrever o destino; evitar “clique aqui”.
- Toda imagem deve ter texto alternativo útil.
- Não transmitir informação apenas por cor.
- Diagramas precisam continuar compreensíveis em impressão monocromática.
- Nomes de assets devem ser minúsculos, sem acentos, descritivos e separados por hífens.

## Revisão editorial

Antes da publicação, verificar:

- cobertura explícita do item do edital;
- correção técnica e atualização das fontes;
- sequência didática e objetivos alcançados;
- consistência terminológica e linguística;
- acessibilidade de links, imagens e tabelas;
- ausência de conteúdo sem atribuição;
- ausência de marcadores provisórios;
- renderização correta no site e nos formatos de exportação aplicáveis.
