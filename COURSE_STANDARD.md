# Padrão definitivo do curso

## Finalidade

Este documento define como construir uma disciplina completa do Curso SAPE/SC. Ele organiza o trabalho. Não substitui os demais manuais.

As regras devem ser lidas nesta ordem:

1. `AGENTS.md`: segurança, escopo e fluxo do repositório;
2. `PEDAGOGY.md`: como fazer a aluna aprender;
3. `STYLE_GUIDE.md`: como escrever e apresentar o conteúdo;
4. `UX.md`: como tornar o estudo simples, inclusive no celular;
5. `COURSE_STANDARD.md`: como montar uma disciplina completa;
6. `QUESTION_GUIDE.md`, `REVIEW_GUIDE.md` e `FEPESE_GUIDE.md`: padrões especializados.

Se duas regras parecerem incompatíveis, não escolha uma em silêncio. Registre o conflito e peça revisão editorial. Nunca reduza clareza, correção, fonte ou respeito aos direitos autorais para cumprir um modelo.

## O que é uma disciplina perfeita

Uma disciplina perfeita cobre integralmente o edital, começa do zero e avança em passos pequenos. A aluna entende onde está, por que estuda cada assunto, como a prova pode cobrá-lo e o que fazer depois.

Ela contém:

- plano da disciplina ligado ao edital;
- módulos em ordem de aprendizagem;
- aulas completas;
- revisões em momentos definidos;
- flashcards próprios para os pontos que precisam ser lembrados;
- questões comentadas por módulo;
- simulado da disciplina;
- fontes verificáveis e registro de revisão.

Quantidade não é sinal de qualidade. Cada recurso precisa ter uma função clara.

## 1. Estrutura da disciplina

### Objetivo

Dar uma visão completa do caminho. Antes da primeira aula, a equipe e a aluna precisam saber o ponto de partida, o ponto de chegada e a ligação de cada módulo com o edital.

### Ordem obrigatória

1. página inicial da disciplina;
2. plano da disciplina;
3. módulos na ordem recomendada;
4. revisão de cada módulo;
5. questões comentadas de cada módulo;
6. revisão final da disciplina;
7. simulado da disciplina;
8. orientação sobre o próximo passo.

### Obrigatoriedade

Toda disciplina deve ter uma matriz que relacione cada item do edital a pelo menos um módulo e uma aula. Um item não pode ficar coberto apenas por questões ou flashcards. A explicação principal deve estar em uma aula.

O plano deve registrar:

- objetivo da disciplina;
- itens do edital;
- módulos e aulas;
- ordem e dependências;
- tempo estimado;
- objetivos de aprendizagem;
- dificuldades esperadas;
- fontes principais;
- estratégia de revisão, questões e flashcards;
- critérios para considerar a disciplina concluída.

### Exemplo

```text
Administração Geral
├── Comece por aqui
├── Módulo 1 • Fundamentos
│   ├── Aula 1 • Primeiro conceito
│   ├── Aula 2 • Segundo conceito
│   ├── Revisão do módulo
│   └── Questões comentadas
├── Módulo 2 • Aplicação
└── Revisão e simulado da disciplina
```

### Checklist da disciplina

- [ ] Todos os itens do edital aparecem na matriz.
- [ ] Não há conteúdo criado apenas porque é comum em outros concursos.
- [ ] A ordem começa pelo que a aluna precisa saber primeiro.
- [ ] Toda dependência é ensinada antes de ser exigida.
- [ ] Os tempos foram estimados para uma iniciante.
- [ ] A navegação mostra o próximo passo.
- [ ] Fontes, responsáveis e datas de revisão estão registrados.

## 2. Estrutura dos módulos

### Objetivo

Reunir aulas que respondem a uma pergunta maior. Um módulo deve formar uma unidade que a aluna consiga estudar, revisar e praticar.

### Ordem obrigatória

1. apresentação do módulo;
2. resultado esperado em linguagem simples;
3. aulas numeradas;
4. revisão curta;
5. questões comentadas;
6. registro de erros;
7. indicação do módulo seguinte.

### Obrigatoriedade

Cada módulo deve ter um tema único e limites claros. Evite módulos definidos apenas pelo tamanho. Uma aula não deve depender de outra que aparece depois.

O encerramento do módulo deve informar o que a aluna já consegue fazer. Também deve indicar o que revisar conforme os erros cometidos.

### Exemplo

```text
Módulo 1 • Fundamentos da Administração Pública
Resultado: reconhecer a estrutura básica da Administração e separar conceitos parecidos.
5 aulas • revisão de 5 minutos • questões comentadas
```

### Checklist do módulo

- [ ] O nome explica o assunto com palavras claras.
- [ ] Existe um resultado observável.
- [ ] As aulas formam uma sequência.
- [ ] O módulo não mistura temas sem ligação.
- [ ] Há revisão e prática ao final.
- [ ] Os erros levam a aulas específicas.

## 3. Estrutura das aulas

### Objetivo

Levar a aluna de uma situação concreta até a aplicação na prova, sem exigir pesquisa externa para compreender a explicação.

### Ordem obrigatória

1. front matter definido no `STYLE_GUIDE.md`;
2. título;
3. cartão com disciplina, módulo, aula, tempo e objetivo;
4. bloco “Nesta aula você vai aprender”;
5. ligação com o edital e com a prova;
6. conhecimentos necessários, explicados de forma breve;
7. exemplo concreto antes de cada conceito importante;
8. explicação simples;
9. termo técnico e caixa “Traduzindo”;
10. aplicação prática;
11. forma de cobrança comprovada ou indicação de que ainda não há evidência suficiente;
12. perguntas durante a explicação;
13. pausas para refletir com resposta esperada;
14. resumo;
15. exercícios de fixação com comentário;
16. checklist;
17. ligação com os flashcards aprovados da aula;
18. fontes e data de revisão;
19. navegação anterior e próxima.

### Obrigatoriedade

Aplicam-se integralmente `PEDAGOGY.md`, `STYLE_GUIDE.md` e `UX.md`. Conceitos importantes exigem exemplo. Termos difíceis exigem explicação antes do nome técnico. A caixa “Pegadinha da FEPESE” só pode existir com evidência oficial registrada conforme `FEPESE_GUIDE.md`.

Se ainda não houver evidência para cumprir uma afirmação específica sobre a FEPESE, a equipe deve ampliar a pesquisa. Nunca deve preencher a lacuna com uma suposição.

### Exemplo de bloco

```markdown
Uma secretaria dividiu o atendimento em três departamentos. Todos continuam dentro da mesma secretaria.

Ela apenas distribuiu tarefas dentro da mesma estrutura.

Esse modo de organizar o trabalho recebe o nome de **desconcentração**.

!!! note "Traduzindo"
    Desconcentrar é dividir tarefas entre órgãos da mesma pessoa jurídica.
```

### Checklist da aula

- [ ] Uma iniciante entende a primeira tela.
- [ ] O objetivo diz o que ela conseguirá fazer.
- [ ] Cada conceito importante começa por um exemplo.
- [ ] Todo termo técnico foi traduzido.
- [ ] Há perguntas e pausas reais.
- [ ] A cobrança da FEPESE tem fonte e tamanho de amostra.
- [ ] Exercícios verificam os objetivos.
- [ ] Resumo, checklist e flashcards cumprem funções diferentes.
- [ ] A aula termina com segurança e próximo passo.
- [ ] A leitura funciona no celular.

## 4. Estrutura dos resumos

### Objetivo

Permitir que a aluna recupere as ideias principais sem reler a aula inteira. Resumo não substitui a primeira leitura.

### Ordem obrigatória

1. ideia principal;
2. regras essenciais;
3. conceitos que podem ser confundidos;
4. exceções previstas na aula;
5. ação necessária para resolver uma questão.

### Obrigatoriedade

Toda aula tem um resumo. Cada módulo e disciplina têm resumos próprios, sem copiar e colar todos os resumos anteriores. O tamanho deve acompanhar a função definida no `REVIEW_GUIDE.md`.

### Exemplo

```text
Órgão é uma parte da estrutura e não possui personalidade jurídica própria.
Entidade é uma pessoa jurídica.
Na prova, pergunte: “Isto é uma parte ou uma pessoa?”
```

### Checklist do resumo

- [ ] Pode ser lido rapidamente.
- [ ] Mantém a precisão técnica.
- [ ] Não introduz assunto novo.
- [ ] Traz o critério que ajuda na prova.
- [ ] Não repete a aula inteira.

## 5. Estrutura dos flashcards

### Objetivo

Fazer a aluna tentar lembrar uma informação antes de ver a resposta. Um flashcard serve para lembrar, não para ensinar um assunto pela primeira vez.

### Ordem obrigatória

1. pergunta com uma única tarefa;
2. pausa para resposta;
3. resposta curta;
4. explicação ou exemplo de uma linha, quando necessário;
5. ligação com aula e item do edital.

### Obrigatoriedade

Crie flashcards apenas para informações que precisam ser lembradas: conceito, regra, exceção, sequência, comparação ou sinal de prova. Não transforme parágrafos em cartões. Mantenha o conjunto principal no local próprio de flashcards. A aula pode mostrar uma seleção ou apontar para esse conjunto, sem criar uma cópia independente.

### Exemplo

```text
Frente: Qual é a pergunta mais rápida para separar órgão de entidade?
Verso: “É uma parte da estrutura ou uma pessoa jurídica?” Órgão é parte; entidade é pessoa.
Origem: Administração Geral, Módulo 1, Aula 2.
```

### Checklist dos flashcards

- [ ] A pergunta aceita uma resposta clara.
- [ ] O cartão testa apenas uma ideia.
- [ ] A resposta cabe em poucas linhas.
- [ ] O cartão não depende de contexto escondido.
- [ ] A origem está registrada.
- [ ] Não existe cartão duplicado com palavras diferentes.

## 6. Estrutura das revisões

### Objetivo

Relembrar, localizar falhas e orientar o retorno ao ponto certo. Revisão não é uma segunda aula completa.

### Ordem obrigatória

1. tentativa de lembrar sem consultar;
2. conferência por resumo ou checklist;
3. aplicação curta;
4. registro do erro;
5. retorno indicado à aula;
6. nova tentativa.

### Obrigatoriedade

Cada aula oferece revisão de 5 minutos. Cada módulo tem revisão própria. Cada disciplina termina com revisão final. A revisão pré-prova reúne somente o conteúdo já ensinado e segue `REVIEW_GUIDE.md`.

### Exemplo

```text
Sem olhar, explique a diferença entre órgão e entidade.
Confira o resumo.
Errou? Volte ao exemplo inicial da Aula 2 e tente outra vez.
```

### Checklist da revisão

- [ ] Começa com tentativa, não com releitura.
- [ ] Indica onde corrigir cada erro.
- [ ] Mistura lembrar e aplicar.
- [ ] Cabe no tempo anunciado.
- [ ] Não apresenta conteúdo novo.

## 7. Estrutura das questões

### Objetivo

Treinar decisão, revelar erros e ensinar o caminho até a resposta.

### Ordem obrigatória

1. identificação clara do tipo;
2. origem e fonte, quando oficial;
3. tema e dificuldade;
4. enunciado;
5. alternativas;
6. espaço para tentativa;
7. resposta recolhível;
8. comentário da correta e de cada errada;
9. erro mais provável;
10. dica prática;
11. ligação com a aula;
12. registro do resultado.

### Obrigatoriedade

Toda questão segue `QUESTION_GUIDE.md`. Questão oficial, oficial adaptada e autoral devem ser identificadas sem ambiguidade. Nenhum gabarito pode ser publicado sem verificação.

### Exemplo curto

```text
Tipo: Questão autoral no estilo de concurso
Tema: órgão e entidade
Dificuldade: fácil — exige reconhecer um conceito direto

Uma secretaria é uma pessoa jurídica própria?

A. Sim.
B. Não.

Resposta: B. A secretaria é um órgão, ou seja, uma parte da estrutura.
```

### Checklist das questões

- [ ] Cobrem todos os objetivos do módulo.
- [ ] Não repetem apenas a mesma definição.
- [ ] Fontes e gabaritos são verificáveis.
- [ ] Cada alternativa recebe comentário específico.
- [ ] A dificuldade tem justificativa.
- [ ] O conjunto não revela padrão de letras.
- [ ] Termos difíceis são traduzidos no comentário.

## 8. Estrutura dos simulados

### Objetivo

Treinar a prova como um conjunto: escolha de ordem, atenção ao comando, controle de tempo e decisão diante de dúvida.

### Ordem obrigatória

1. objetivo e escopo;
2. número de questões, pesos e tempo;
3. instruções iguais às condições que estão sendo treinadas;
4. questões sem comentários visíveis;
5. folha de respostas;
6. gabarito separado;
7. comentários completos;
8. tabela de resultados por assunto;
9. plano de revisão após o resultado.

### Obrigatoriedade

O simulado deve refletir a estrutura oficial quando ela estiver definida. Qualquer diferença precisa ser avisada antes do início. Questões usadas em aulas e listas não devem reaparecer no simulado principal.

### Exemplo de instrução

```text
Este simulado cobre os três módulos da disciplina. Reserve 40 minutos. Responda sem consultar as aulas. Ao terminar, corrija por assunto, não apenas pelo total de acertos.
```

### Checklist do simulado

- [ ] Escopo e tempo estão claros.
- [ ] Quantidade e peso seguem o edital ou têm diferença informada.
- [ ] Não há questões já conhecidas no simulado principal.
- [ ] Dificuldades e letras estão equilibradas.
- [ ] O gabarito foi conferido por outra pessoa.
- [ ] Cada erro leva a uma aula ou revisão.
- [ ] O resultado produz um próximo passo claro.

## Controle final de qualidade

Uma disciplina só pode ser considerada pronta quando passar por quatro revisões independentes:

1. **técnica:** conteúdo, lei, edital e gabaritos;
2. **pedagógica:** exemplos, sequência, perguntas e aprendizagem;
3. **editorial:** linguagem, consistência e direitos autorais;
4. **experiência da aluna:** celular, navegação, tempo e clareza do próximo passo.

Checklist final:

- [ ] A disciplina cobre integralmente o edital.
- [ ] Não há conhecimento exigido antes de ser ensinado.
- [ ] A aluna pratica todos os objetivos.
- [ ] As análises da FEPESE seguem `FEPESE_GUIDE.md`.
- [ ] Questões e simulados seguem `QUESTION_GUIDE.md`.
- [ ] Revisões seguem `REVIEW_GUIDE.md`.
- [ ] Todas as fontes estão acessíveis e datadas.
- [ ] Não há conteúdo de terceiros reproduzido além do necessário.
- [ ] Não há padrões previsíveis nos gabaritos.
- [ ] A aluna sempre sabe o que fazer depois.
- [ ] Uma iniciante consegue estudar sem pedir ajuda.
