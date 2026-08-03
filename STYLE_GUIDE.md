# Guia de estilo editorial

Este documento define a filosofia editorial e o padrão obrigatório das aulas do curso SAPE/SC.

## Princípios

O curso é escrito para uma pessoa inteligente que está estudando o assunto pela primeira vez. O texto deve ser correto, direto, progressivo, rastreável e orientado ao edital. Clareza prevalece sobre ornamentação.

Não basta apresentar informação correta. A aula precisa conduzir o aluno do exemplo concreto ao conceito técnico. Depois, deve mostrar como reconhecer e aplicar o conceito em uma questão.

Cada explicação deve ajudar o estudante a compreender, recordar ou aplicar um ponto claramente identificado. Nunca use a complexidade do assunto como justificativa para uma explicação difícil de acompanhar.

## Linguagem

- Escrever em português brasileiro conforme a norma-padrão vigente.
- Usar frases curtas.
- Evitar períodos longos. Dividir uma ideia complexa em etapas quando necessário.
- Evitar palavras difíceis quando existir uma alternativa simples e precisa.
- Explicar todo termo técnico em linguagem simples na primeira ocorrência.
- Nunca presumir conhecimento prévio do aluno.
- Usar tom profissional, acolhedor e seguro, sem promessas de aprovação.
- Preferir voz ativa e verbos concretos.
- Explicar siglas na primeira ocorrência.
- Evitar jargão desnecessário, humor que envelheça rapidamente e linguagem depreciativa.
- Tratar o leitor por “você” quando a orientação direta melhorar a compreensão.

Uma frase simples não é uma frase imprecisa. Preserve os termos exigidos pela lei, pelo edital ou pela técnica. Apresente primeiro o significado em linguagem natural. Depois, introduza a formulação técnica.

## Linguagem proibida

Não usar construções artificiais, burocráticas ou excessivamente formais quando houver forma natural equivalente. As seguintes expressões estão proibidas no texto didático:

- “revisar a distinção central”;
- “conforme observado anteriormente”;
- “destarte”;
- “outrossim”;
- “mister se faz”;
- “nesse diapasão”;
- “destaca-se”;
- “cumpre salientar”.

Substitua-as por uma orientação direta. Exemplos:

| Evite | Prefira |
|---|---|
| Revisar a distinção central | Volte à diferença entre os dois conceitos |
| Conforme observado anteriormente | Como vimos na seção anterior |
| Destarte | Por isso |
| Outrossim | Além disso |
| Mister se faz | É necessário |
| Nesse diapasão | Nesse contexto |
| Destaca-se | O ponto principal é |
| Cumpre salientar | Observe que |

## Objetivo da aula

Toda aula deve responder com clareza, logo no início:

- O que você vai aprender?
- Por que isso cai na prova?
- Como a FEPESE cobra esse assunto?
- Como identificar as pegadinhas relacionadas ao assunto?

Transforme essas respostas em objetivos verificáveis. Evite objetivos vagos como “conhecer o tema” ou “entender a matéria”. Prefira verbos que indiquem uma ação observável, como identificar, distinguir, calcular, classificar, interpretar ou aplicar.

Quando o edital não permitir explicar por que um tópico tem determinada incidência, informe apenas que ele consta do programa. Não invente frequência, tendência ou relevância estatística.

## Didática

### Sequência didática

Sempre que a natureza do assunto permitir, desenvolva cada conceito importante nesta ordem:

1. **Exemplo do mundo real:** apresente uma situação concreta que crie o problema.
2. **Explicação simples:** explique a ideia com palavras comuns.
3. **Conceito técnico:** introduza o nome, a definição e os limites técnicos.
4. **Como a FEPESE costuma cobrar:** mostre formatos de cobrança observados em questões oficiais.
5. **Pegadinhas da banca:** apresente confusões e armadilhas comprovadas em questões oficiais.
6. **Resumo:** recupere a regra, as distinções e o procedimento.
7. **Exercícios:** exija que o aluno reconheça ou aplique o conceito.

Se a sequência não servir a um tópico específico, preserve sua finalidade: começar pelo concreto, construir a explicação e terminar com aplicação verificável. Registre a razão editorial quando uma etapa for omitida.

Afirmações sobre o comportamento da FEPESE devem ser sustentadas por questões oficiais identificadas. Não atribua uma “pegadinha da banca” à FEPESE apenas porque o tema admite confusão. Se ainda não houver amostra suficiente, descreva a confusão como ponto de atenção e marque a análise da banca como pendência editorial, nunca como fato.

## Exemplos

Todo conceito importante deve possuir pelo menos um exemplo prático. O exemplo deve aparecer próximo da explicação correspondente.

Use situações plausíveis e específicas:

- atividades do cotidiano;
- rotinas da Administração Pública;
- decisões, processos e documentos de empresas;
- situações funcionais compatíveis com o cargo, quando a relação for real.

O exemplo deve demonstrar o conceito, e não apenas trocar os nomes de uma definição abstrata. Informe todos os dados necessários. Depois do exemplo, explique por que ele representa a regra e onde o aluno poderia se confundir.

Exemplos autorais devem ser identificáveis como exemplos, não como fatos do concurso. Não invente órgãos, estatísticas, decisões, programas públicos ou casos reais. Quando criar uma situação hipotética, deixe isso claro.

## Estrutura obrigatória de uma aula

Cada futura aula deverá conter, nesta ordem:

1. front matter YAML;
2. título único de nível 1;
3. objetivos de aprendizagem verificáveis e respostas às quatro perguntas de objetivo da aula;
4. vínculo com os itens do edital e justificativa de cobrança;
5. pré-requisitos explicados sem presumir que foram dominados;
6. desenvolvimento organizado conforme a sequência didática;
7. exemplos práticos autorais ou devidamente licenciados;
8. forma de cobrança da FEPESE, sustentada por questões oficiais;
9. dicas e pegadinhas verificadas;
10. resumo para revisão;
11. exercícios de fixação;
12. checklist final;
13. referências e data da última revisão.

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

## Quadros visuais

Use caixas do Markdown/MkDocs com títulos e funções consistentes.

### Dica

Use para uma estratégia prática de compreensão, memorização ou resolução.

```markdown
!!! tip "Dica"
    Texto da dica.
```

### Pegadinha da FEPESE

Use apenas quando a armadilha estiver sustentada por questão oficial identificada.

```markdown
!!! warning "Pegadinha da FEPESE"
    Explique a armadilha, a resposta correta e o motivo do erro.
```

### Importante

Use para uma regra, condição ou distinção necessária à compreensão.

```markdown
!!! note "Importante"
    Texto da informação importante.
```

### Exemplo

Use para uma aplicação concreta do conceito.

```markdown
!!! example "Exemplo"
    Apresente a situação e explique a aplicação.
```

Outros tipos de admonition permanecem disponíveis somente quando houver necessidade clara:

- `danger`: erro grave capaz de invalidar uma resposta;
- `question`: exercício curto que exige resposta antes da continuação.

Não acumule caixas de destaque. Uma informação central deve permanecer no fluxo principal. Não use uma caixa apenas para decorar a página.

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
- compreensão possível para uma pessoa sem conhecimento prévio na primeira leitura;
- explicação simples de todo termo técnico na primeira ocorrência;
- pelo menos um exemplo prático para cada conceito importante;
- pelo menos uma caixa `tip` com o título “Dica”;
- pelo menos uma caixa `warning` com o título “Pegadinha da FEPESE”, sustentada por questão oficial;
- resumo suficiente para recuperação dos pontos centrais;
- checklist final com ações verificáveis;
- exercício de fixação com resposta ou mecanismo de correção;
- explicação de como a FEPESE cobra, sustentada por questões oficiais;
- consistência terminológica e linguística;
- acessibilidade de links, imagens e tabelas;
- ausência de conteúdo sem atribuição;
- ausência de marcadores provisórios;
- renderização correta no site e nos formatos de exportação aplicáveis.

### Perguntas de controle de qualidade

Antes de considerar uma aula pronta, responda:

- Uma pessoa sem conhecimento prévio entenderia na primeira leitura?
- Existe pelo menos um exemplo?
- Existe pelo menos uma dica?
- Existe pelo menos uma pegadinha?
- Existe um resumo?
- Existe um checklist?
- Existe exercício de fixação?

Se qualquer resposta for “não”, a aula permanece em revisão. Quando ainda não houver evidência oficial para uma pegadinha atribuível à FEPESE, amplie a análise de questões antes da publicação. Nunca invente um padrão da banca apenas para completar o checklist.
