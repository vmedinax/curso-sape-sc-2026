# Manual oficial de questões

## Finalidade

Este documento define como selecionar, criar, comentar e organizar questões do Curso SAPE/SC. Ele aplica as regras de `AGENTS.md`, `PEDAGOGY.md`, `STYLE_GUIDE.md`, `UX.md`, `COURSE_STANDARD.md` e `FEPESE_GUIDE.md`.

Uma questão não serve apenas para contar acertos. Ela deve mostrar o que a aluna compreendeu, onde errou e qual passo deve dar para corrigir o erro.

## Tipos permitidos

Use exatamente uma destas classificações:

- **Questão oficial FEPESE:** reprodução curta e autorizada ou permitida, sem alteração de sentido, com origem e gabarito oficial verificados.
- **Questão oficial adaptada:** questão oficial transformada de modo claro, sem ser apresentada como texto original.
- **Questão autoral no estilo de concurso:** criada para o curso, sem atribuir à FEPESE uma característica não comprovada.

Se houver dúvida sobre a classificação, não publique até a revisão de fontes e direitos autorais.

## 1. Como selecionar questões oficiais

### Objetivo

Usar evidência real para treinar o conteúdo e estudar a banca.

### Ordem de seleção

1. confirme o item do edital e o objetivo da aula;
2. procure em páginas oficiais da FEPESE e do concurso;
3. localize o caderno completo;
4. localize o gabarito definitivo;
5. confirme concurso, órgão, cargo, ano e número;
6. verifique se a questão realmente avalia o assunto;
7. registre a fonte antes de incluí-la;
8. avalie direitos autorais e necessidade de adaptação;
9. faça revisão técnica do gabarito e do comentário.

### Fonte mínima

Cada questão oficial deve registrar:

- banca;
- concurso e edital;
- órgão;
- cargo;
- ano;
- número original;
- assunto e parte específica do assunto;
- página do caderno;
- endereço do caderno;
- endereço do gabarito definitivo;
- resposta oficial;
- data de consulta;
- situação da fonte: acessível, substituída, retirada ou arquivada.

Se apenas um caderno com respostas marcadas for encontrado, informe isso. Não chame a marcação de gabarito definitivo sem documento que sustente essa afirmação.

### Critérios de exclusão

Não use a questão quando:

- a origem não puder ser confirmada;
- o gabarito oficial não puder ser verificado ou explicado;
- o assunto estiver fora da aula ou do módulo;
- a adaptação necessária destruir o conhecimento avaliado;
- houver imagem indispensável sem permissão de uso;
- a norma usada estiver revogada e a questão não tiver função histórica clara;
- o enunciado depender de conteúdo que a aluna ainda não estudou.

Registre questões descartadas e o motivo. Isso evita repetir pesquisas e decisões.

## 2. Quando adaptar uma questão

### Adapte quando

- a reprodução integral não for necessária;
- houver risco de uso excessivo de texto de terceiros;
- o enunciado contiver nomes, trechos ou imagens que possam ser substituídos;
- a norma mudou, mas o conhecimento central ainda puder ser treinado com aviso claro;
- o texto precisar ser reduzido para acessibilidade sem alterar a tarefa mental.

### Não adapte quando

- uma palavra exata for o objeto da questão e a mudança alterar o gabarito;
- a adaptação fizer parecer que a FEPESE escreveu texto criado pelo curso;
- não for possível explicar o que mudou;
- a questão puder ser apenas referenciada e descrita com segurança.

### Regra de transformação

Não basta trocar nomes. Uma boa adaptação preserva o conhecimento avaliado, mas cria nova situação e nova redação. Quando houver dúvida, prefira:

1. descrição fiel do problema;
2. link para o caderno oficial;
3. pergunta autoral sobre o mesmo conhecimento;
4. comentário completo.

### Nota obrigatória

```text
Questão oficial adaptada. O texto foi reescrito para fins didáticos. Consulte a questão original na fonte indicada.
```

## 3. Quando criar questão autoral

Crie uma questão autoral quando:

- não houver questão oficial adequada;
- um objetivo da aula ainda não estiver coberto;
- for necessário começar com aplicação mais simples;
- a aluna precisar comparar conceitos em uma situação nova;
- a lista precisar de equilíbrio de temas e dificuldades;
- uma norma atualizada exigir novo enunciado.

A questão autoral pode usar formatos observados em provas. Ela não pode ser apresentada como padrão da FEPESE sem a análise exigida por `FEPESE_GUIDE.md`.

## 4. Como citar fontes

### No arquivo de pesquisa

Registre todos os campos da fonte mínima, a justificativa de uso e qualquer transformação feita.

### Na página da aluna

Mostre de forma curta:

```text
Origem: FEPESE • Concurso X • Cargo Y • 2025 • Questão 26
Fonte oficial: Caderno de prova | Gabarito definitivo
```

Detalhes extensos podem ficar em caixa recolhível para não ocupar a primeira tela no celular.

### Regras

- use link direto para o documento, não para resultado de busca;
- registre a data de consulta;
- não copie logotipo, página inteira ou imagem sem necessidade e permissão;
- citações literais devem ser curtas e atribuídas;
- uma questão adaptada continua exigindo citação;
- guarde a diferença entre resposta oficial e análise do curso.

## 5. Estrutura de cada questão

```markdown
## Questão X

**Tipo:** Questão autoral no estilo de concurso

**Dificuldade:** fácil

[Enunciado]

A. ...
B. ...
C. ...
D. ...
E. ...

Pare e escolha uma resposta antes de abrir o comentário.

??? question "Mostrar resposta e comentário"
    **Tema cobrado:** órgão e entidade

    **Resposta:** C.

    **Explicação simples:** ...

    **Termo usado na prova:** ...

    **Por que C está certa:** ...

    **Por que A está errada:** ...

    **Por que B está errada:** ...

    **Por que D está errada:** ...

    **Por que E está errada:** ...

    **Aula para revisar:** ...

    **Erro mais provável:** ...

    **Dica VX:** ...
```

## 6. Como construir alternativas

Todas as alternativas devem ser plausíveis para quem ainda confunde o assunto. Uma alternativa errada precisa conter um erro identificável.

Regras:

- mantenha tamanho e forma parecidos;
- evite uma correta muito mais detalhada que as outras;
- não use humor ou opções absurdas;
- não crie duas respostas defensáveis;
- não esconda o erro apenas em redação confusa;
- use “sempre”, “nunca”, “somente” e termos parecidos apenas quando fizerem sentido técnico;
- não transforme toda palavra absoluta em pista automática;
- revise negações como “incorreta” e “exceto” com atenção especial;
- em afirmações combinadas, confira todas as combinações.

## 7. Como comentar cada alternativa

O comentário deve ensinar a decisão. Não basta dizer que a opção está certa ou errada.

Para cada alternativa:

1. identifique a ideia usada;
2. mostre o trecho decisivo;
3. explique a regra com palavras simples;
4. apresente o termo técnico;
5. diga como corrigir a frase errada, quando isso ajudar.

### Evite

```text
A alternativa B está incorreta.
```

### Prefira

```text
B está errada porque afirma que a tarefa foi entregue a outra pessoa jurídica. No caso, a divisão ocorreu dentro da mesma secretaria. A pessoa jurídica não mudou. Isso é desconcentração.
```

Não agrupe opções com frases como “A, B e D não correspondem ao conceito” quando os erros forem diferentes. Explique uma por uma.

## 8. Como explicar o erro da aluna

O comentário deve indicar o caminho mental que pode ter levado ao erro, sem culpar a aluna.

Categorias úteis:

- confundiu termos parecidos;
- não percebeu uma negação;
- reconheceu uma palavra e parou de ler;
- aplicou uma regra correta ao caso errado;
- ignorou uma exceção;
- escolheu opção parcialmente verdadeira;
- usou informação de outra aula;
- não separou fato do caso e regra jurídica.

### Modelo

```text
Erro mais provável: você viu a palavra “divisão” e pensou em descentralização. Antes de decidir, confira se surgiu outra pessoa jurídica. Se não surgiu, pense em desconcentração.
```

## 9. Como indicar a aula correspondente

Toda questão deve apontar para o lugar exato que ensina a resposta:

```text
Aula para revisar: Administração Geral • Módulo 1 • Aula 2 • seção “Descentralização e desconcentração”.
```

Não use apenas “conforme estudado”. O link deve funcionar e o título precisa continuar compreensível fora do contexto.

Se a resposta depender de duas aulas, indique as duas. Se não houver aula correspondente, a questão não está pronta para aquela lista.

## 10. Como escrever dicas da prova

Uma dica deve oferecer uma ação segura:

```text
Dica VX: antes de escolher, circule mentalmente quem realiza a atividade. Se continua sendo a mesma pessoa jurídica, descarte descentralização.
```

Não use:

- promessa de acerto;
- regra que falha diante de exceções;
- pista baseada no tamanho da alternativa;
- truque sem relação com o conteúdo;
- “a FEPESE gosta” sem análise suficiente.

“Pegadinha da FEPESE” exige a evidência definida em `FEPESE_GUIDE.md`. Uma confusão didática pode ser chamada de “Isso costuma confundir”, sem atribuição à banca.

## 11. Como medir dificuldade

A dificuldade é estimada para uma aluna que concluiu as aulas correspondentes.

### Fácil

Exige uma ideia, comando direto e pouco texto. Normalmente pede reconhecer ou lembrar.

### Média

Exige comparar duas ideias, aplicar uma regra a um caso ou perceber uma palavra decisiva.

### Difícil

Exige combinar três ou mais ideias, lidar com exceção relevante, interpretar caso longo ou completar várias etapas de raciocínio.

### Registro obrigatório

Não escreva apenas “média”. Justifique:

```text
Dificuldade: média — exige separar órgão de entidade e depois identificar a forma de organização.
```

A classificação deve ser revista após uso. Se muitas alunas com domínio do conteúdo errarem pelo mesmo problema de redação, corrija a questão antes de aumentar sua dificuldade.

## 12. Como distribuir alternativas corretas

Em listas e simulados com cinco alternativas, busque distribuição próxima entre A, B, C, D e E.

Regras:

- a diferença entre a letra mais usada e a menos usada deve ser, em regra, no máximo uma questão quando o total permitir;
- não use a mesma letra correta três vezes seguidas;
- não crie sequência visível, como A-B-C-D-E repetida;
- não altere gabarito de questão oficial para equilibrar letras;
- faça o equilíbrio nas questões autorais e na seleção das oficiais;
- confira também padrões por tema e dificuldade.

Em uma lista de 20 questões, uma boa referência é quatro respostas por letra. Isso não precisa formar uma sequência.

## 13. Como evitar repetição e padrões previsíveis

Antes de publicar, monte uma matriz com:

| Questão | Tema | Ação exigida | Dificuldade | Letra | Origem |
|---|---|---|---|---|---|

Confira:

- se um assunto importante ficou sem questão;
- se muitas questões pedem apenas definição;
- se o mesmo caso foi apenas reescrito;
- se uma letra domina o gabarito;
- se todas as difíceis ficaram no final;
- se questões oficiais e autorais podem ser identificadas pelo estilo;
- se o tamanho da correta dá pista.

Repetição é válida quando muda a ação: primeiro reconhecer, depois comparar e por fim aplicar. Repetir a mesma pergunta com outros nomes não acrescenta treino.

## 14. Exemplo completo

### Questão-modelo

**Tipo:** Questão autoral no estilo de concurso

**Dificuldade:** média

Uma secretaria estadual criou dois departamentos internos. Um passou a cuidar dos contratos. O outro ficou responsável pelo atendimento. Os dois continuam subordinados à mesma secretaria.

Essa organização representa:

A. descentralização, porque as tarefas foram divididas.

B. privatização, porque cada departamento recebeu uma função.

C. desconcentração, porque as tarefas foram distribuídas dentro da mesma pessoa jurídica.

D. criação de duas autarquias, porque os departamentos possuem assuntos próprios.

E. delegação para particulares, porque a secretaria deixou de executar todas as tarefas diretamente.

Pare e escolha uma resposta antes de abrir o comentário.

??? question "Mostrar resposta e comentário"
    **Tema cobrado:** desconcentração e descentralização

    **O que você precisava perceber:** a permanência das unidades na mesma pessoa jurídica caracteriza desconcentração.

    **Resposta:** C.

    **Explicação simples:** a secretaria dividiu o trabalho dentro da própria estrutura. Nenhuma nova pessoa foi criada e nenhum particular recebeu a atividade.

    **Termo usado na prova:** **desconcentração**. Isso significa distribuir competências entre órgãos da mesma pessoa jurídica.

    **Por que C está certa:** os departamentos são partes internas da mesma secretaria. Esse é o sinal da desconcentração.

    **Por que A está errada:** dividir tarefas não basta para existir descentralização. Seria necessário entregar a atividade a outra pessoa jurídica.

    **Por que B está errada:** privatização envolve transferência para o setor privado. O caso continua inteiramente dentro do Estado.

    **Por que D está errada:** departamento é órgão interno. Autarquia é uma pessoa jurídica criada por lei.

    **Por que E está errada:** nenhum particular aparece no caso. A secretaria apenas reorganizou suas unidades.

    **Aula para revisar:** Administração Geral • Módulo 1 • Aula 2 • seção “Descentralização e desconcentração”.

    **Erro mais provável:** escolher A apenas porque o enunciado fala em divisão de tarefas.

    **Dica VX:** pergunte se apareceu outra pessoa jurídica. Se a resposta for não, procure a desconcentração.

## 15. Como construir simulados

O simulado segue também `COURSE_STANDARD.md`.

### Projeto do simulado

Antes de escrever questões, defina:

- edital e data de corte;
- disciplinas e itens cobrados;
- quantidade e peso oficiais;
- tempo;
- nível esperado;
- matriz por assunto e ação exigida;
- proporção de questões oficiais, adaptadas e autorais;
- plano de correção.

### Montagem

1. cubra a matriz, não a preferência do autor;
2. misture assuntos como ocorrerá na prova;
3. não reutilize questões já respondidas no curso principal;
4. mantenha comentários ocultos até o final;
5. equilibre letras e dificuldades;
6. confira comandos negativos;
7. faça uma resolução independente;
8. revise o gabarito com outra pessoa;
9. teste o tempo com uma leitora do perfil da aluna;
10. gere relatório por assunto e aula.

### Resultado

O total de acertos não basta. O relatório deve mostrar:

- acertos por disciplina e assunto;
- erros por tipo;
- questões deixadas em branco;
- tempo usado;
- aulas a revisar;
- nova tentativa recomendada.

Não invente progresso automático. Se o sistema for manual, ofereça campos simples para a própria aluna preencher.

## Auditoria antes da publicação

- [ ] Toda questão está dentro do edital e foi ensinada.
- [ ] Questões oficiais têm caderno e gabarito verificados.
- [ ] A classificação da origem está correta.
- [ ] A reprodução de terceiros foi reduzida ao necessário.
- [ ] Cada alternativa tem comentário próprio.
- [ ] O comentário explica e traduz termos.
- [ ] Cada erro leva a uma aula específica.
- [ ] A dificuldade tem motivo.
- [ ] Temas, ações e letras estão equilibrados.
- [ ] Não há sequência previsível de respostas.
- [ ] Afirmações sobre a FEPESE seguem `FEPESE_GUIDE.md`.
- [ ] A página funciona no celular.
- [ ] Outra pessoa conferiu o gabarito.
