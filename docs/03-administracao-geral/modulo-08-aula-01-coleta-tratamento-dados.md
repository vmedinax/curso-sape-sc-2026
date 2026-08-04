---
id: administracao-geral-modulo-08-aula-01
title: "Coleta, organização e tratamento de dados"
discipline: 03-administracao-geral
module: 8
lesson: 1
status: draft
edital_refs: [anexo-2-administracao-geral-coleta-organizacao-tratamento-dados]
prerequisites: [administracao-geral-modulo-08]
estimated_minutes: 90
authors: [Equipe do Curso SAPE/SC]
reviewers: []
last_reviewed: null
sources:
  - https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/governanca-de-dados
tags: [dados, coleta, tratamento]
---

# Aula 1 — Coleta, organização e tratamento de dados

<section class="lesson-goal"><h2>Nesta aula você vai aprender</h2><p>a coletar e preparar dados sem esconder erros, misturar conceitos ou mudar o sentido dos registros.</p></section>

<div class="lesson-meta-grid"><div class="lesson-meta-card"><span>Disciplina</span><strong>Administração Geral</strong></div><div class="lesson-meta-card"><span>Módulo</span><strong>8 • Informação e documentos</strong></div><div class="lesson-meta-card"><span>Aula</span><strong>1 de 8</strong></div><div class="lesson-meta-card"><span>Tempo</span><strong>90 minutos</strong></div></div>

## Uma planilha com três respostas para a mesma pergunta

Três unidades registram o município como “Florianópolis”, “Fpolis” e “FLN”. O sistema entende três lugares diferentes. Antes de contar atendimentos por município, a equipe precisa organizar os registros.

## Dado e informação

**Dado** é um registro bruto, como data, valor ou categoria. **Informação** é dado organizado e interpretado para responder uma pergunta.

!!! example "Exemplo"
    “12” é dado. “Prazo médio de 12 dias em julho” é informação porque possui contexto.

## Planejar a coleta

Antes de coletar, defina:

- pergunta que será respondida;
- unidade observada;
- variável;
- período;
- fonte;
- responsável;
- forma e frequência do registro;
- regras de qualidade e proteção.

**Variável** é uma característica que pode assumir valores diferentes, como município ou prazo.

!!! note "Traduzindo"
    Unidade observada é aquilo sobre o que cada linha fala: uma pessoa, um pedido, uma propriedade ou um atendimento.

## Fontes primárias e secundárias

- **primária:** dado coletado diretamente para a análise, como entrevista feita pela equipe;
- **secundária:** dado já existente, como cadastro administrativo.

Uma fonte secundária pode ser útil, mas foi criada para outra finalidade. Confira conceitos, cobertura e atualidade.

## Tratar os dados

Tratamento pode incluir:

- padronizar formatos;
- retirar duplicidades verdadeiras;
- verificar valores impossíveis;
- lidar com campos vazios;
- combinar bases com chave adequada;
- documentar mudanças;
- proteger dados pessoais.

!!! warning "Isso costuma confundir"
    Limpar dados não significa apagar tudo que parece estranho. Um valor extremo pode ser erro ou caso real importante.

## Dados ausentes

Campo vazio pode significar informação desconhecida, não aplicável, não coletada ou perdida. Misturar esses motivos cria erro.

Nunca substitua automaticamente todo vazio por zero. Zero é um valor; ausência é falta de registro.

!!! tip "Dica VX"
    Pergunte o significado de cada vazio antes de decidir como tratá-lo.

## Duplicidade

Duas linhas iguais podem representar repetição indevida ou dois eventos reais. Use identificadores, datas e regras do serviço para decidir.

## Metadados

São dados que explicam outros dados: nome do campo, conceito, formato, fonte, data de atualização e responsável.

!!! note "Traduzindo"
    Metadado é a etiqueta explicativa do dado.

## Qualidade dos dados

Observe:

- completude: campos necessários preenchidos;
- exatidão: registro corresponde ao fato;
- consistência: regras e valores não se contradizem;
- atualidade: dado está atualizado;
- unicidade: não há repetição indevida;
- rastreabilidade: é possível saber origem e mudanças.

## Resumo

- Dado ganha sentido quando recebe contexto.
- Coleta começa pela pergunta.
- Variáveis e unidades precisam ser claras.
- Tratar não é esconder casos difíceis.
- Vazio não é zero.
- Metadados explicam origem e significado.

## Checklist

- [ ] Separo dado e informação.
- [ ] Defino unidade e variável.
- [ ] Separo fonte primária e secundária.
- [ ] Trato vazio e duplicidade com regra.
- [ ] Registro origem e alterações.

## Exercícios de fixação

### 1. Um campo vazio deve virar zero automaticamente?
### 2. O que são metadados?
### 3. Dê exemplo de variável.

??? question "Ver gabarito comentado"
    **1. Não.** Vazio pode ter vários sentidos. **2.** Dados que explicam outros dados. **3.** Município, prazo ou tipo de atendimento.

## Flashcards da aula

??? question "O que é dado?"
    Registro bruto de um fato ou característica.
??? question "O que é informação?"
    Dado organizado e interpretado em contexto.
??? question "Vazio é zero?"
    Não.
??? question "O que são metadados?"
    Dados que explicam significado, origem e formato de outros dados.

[← Apresentação](modulo-08-index.md){ .md-button }

[Próxima aula →](modulo-08-aula-02-interpretacao-estatistica.md){ .md-button .md-button--primary }
