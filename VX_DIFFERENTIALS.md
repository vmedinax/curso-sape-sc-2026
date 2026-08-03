# Diferenciais competitivos da VX

## Finalidade

Este documento registra somente diferenciais que podem gerar valor real para a aluna, podem ser implementados neste projeto e não dependem de copiar conteúdo, identidade ou funcionamento interno de terceiros.

Um item só permanece nesta lista quando atende aos três critérios.

## Diferenciais atuais

### 1. Curso realmente escrito para quem começa do zero

**Valor para a aluna:** reduz o medo inicial e evita que uma palavra técnica bloqueie o restante da explicação.

**Como funciona:** o curso parte de uma situação concreta, explica a ideia com palavras comuns e só depois apresenta o termo usado na prova.

**Por que é implementável:** o padrão já está definido em `PEDAGOGY.md` e aplicado no primeiro módulo.

**Por que é próprio:** nasce do perfil específico da aluna e das regras editoriais da VX.

### 2. Experiência de professora particular no texto

**Valor para a aluna:** mantém a atenção e antecipa dúvidas que normalmente interromperiam o estudo.

**Como funciona:** cada aula conversa com a aluna, faz perguntas durante a explicação, cria pausas para pensar e mostra uma resposta esperada.

**Por que é implementável:** depende de autoria, revisão pedagógica e modelos já documentados.

**Por que é próprio:** não depende de vídeo, personalidade pública ou texto de outro curso.

### 3. Tradução imediata da linguagem da prova

**Valor para a aluna:** permite aprender o vocabulário técnico sem precisar pesquisar fora do curso.

**Como funciona:** a ideia simples aparece antes do termo. A caixa “Traduzindo” consolida o significado e oferece um exemplo quando necessário.

**Por que é implementável:** pode ser auditado em cada aula e em cada comentário de questão.

**Por que é próprio:** a tradução é produzida pela VX para o contexto exato do edital.

### 4. Cobertura rastreável do edital

**Valor para a aluna:** reduz o risco de estudar assunto irrelevante ou deixar um ponto oficial sem explicação.

**Como funciona:** edital, mapa do curso, plano da disciplina, módulos, aulas, questões e revisões são ligados entre si.

**Por que é implementável:** Markdown e metadados permitem manter essa relação sem plataforma cara.

**Por que é próprio:** usa somente o edital oficial e a estrutura editorial do projeto.

### 5. Análise da FEPESE com evidência declarada

**Valor para a aluna:** evita decorar supostas manias da banca que não foram comprovadas.

**Como funciona:** toda conclusão informa número de questões, concursos, anos, evidências, exceções e limites da amostra.

**Por que é implementável:** o modelo de pesquisa está definido em `FEPESE_GUIDE.md`.

**Por que é próprio:** o diferencial está no rigor da análise, não na reprodução das provas.

### 6. Questão comentada como aula de correção

**Valor para a aluna:** transforma cada erro em uma orientação concreta de estudo.

**Como funciona:** cada alternativa recebe explicação própria. O comentário traduz termos, identifica o erro provável e aponta a aula e a seção para revisar.

**Por que é implementável:** o formato já está validado no Módulo 1 de Administração Geral.

**Por que é próprio:** casos e comentários autorais são construídos a partir dos objetivos da aula.

### 7. Respeito claro à origem das questões

**Valor para a aluna:** permite saber o que é oficial, adaptado ou criado pelo curso.

**Como funciona:** o projeto separa questão oficial adaptada de questão autoral, registra caderno e gabarito e declara quando uma fonte definitiva não foi localizada.

**Por que é implementável:** exige controle editorial, não licença de uma plataforma externa.

**Por que é próprio:** a VX preserva o conhecimento cobrado sem reconstruir desnecessariamente o material de terceiros.

### 8. Caminho completo dentro de cada módulo

**Valor para a aluna:** elimina a dúvida sobre o que fazer depois da aula.

**Como funciona:** aula, questões comentadas, revisão de 5 minutos, mapa mental e simulado formam uma sequência visível.

**Por que é implementável:** o primeiro módulo já fornece o modelo.

**Por que é próprio:** a sequência foi criada para a arquitetura e para o perfil de aluna da VX.

### 9. Correção orientada pelo tipo de erro

**Valor para a aluna:** diferencia falta de conteúdo, confusão entre conceitos, leitura apressada e acerto por chute.

**Como funciona:** tabelas simples levam cada erro ao ponto exato de revisão.

**Por que é implementável:** pode começar manualmente e evoluir depois para um painel.

**Por que é próprio:** as categorias de erro acompanham as aulas e questões da VX.

### 10. Plataforma limpa e pensada para celular

**Valor para a aluna:** reduz distrações e facilita estudar em intervalos curtos.

**Como funciona:** menu em árvore, conteúdo central, botões claros, parágrafos curtos e ausência de elementos técnicos que competem com a aula.

**Por que é implementável:** a base atual já suporta esse desenho.

**Por que é próprio:** as decisões respondem ao perfil real da aluna do projeto.

### 11. Uma única fonte para site, PDF e Word

**Valor para a aluna:** reduz diferenças entre versões e facilita acesso no formato disponível.

**Como funciona:** o Markdown é a fonte principal e os outros formatos serão gerados a partir dele.

**Por que é implementável:** a arquitetura já foi planejada para geração automática.

**Por que é próprio:** é uma decisão técnica do repositório.

## Diferenciais futuros

### 12. Três planos semanais por tempo disponível

**Valor para a aluna:** responde “o que estudo esta semana?” sem criar uma rotina impossível.

**Implementação possível:** oferecer rotas de 5, 10 e 15 horas semanais, sempre ligadas às mesmas aulas, revisões e questões.

**Regra própria:** os planos serão calculados com os tempos da VX e ajustados ao edital SAPE/SC.

### 13. Agenda de revisão flexível

**Valor para a aluna:** lembra quando retomar o assunto e evita acumular revisões que não cabem na rotina.

**Implementação possível:** começar com tabelas marcáveis para revisão no dia seguinte, após uma semana e após um mês. Permitir antecipar ou adiar conforme o erro.

**Regra própria:** o calendário orienta. O desempenho da aluna decide a próxima revisão.

### 14. Painel simples de progresso e cobertura

**Valor para a aluna:** mostra aulas concluídas, questões respondidas, acertos, revisões pendentes e itens do edital cobertos.

**Implementação possível:** primeira versão local e manual, sem conta externa. Versões futuras podem salvar dados no navegador com consentimento.

**Regra própria:** progresso não será medido apenas por páginas abertas. A aluna registra compreensão, prática e revisão.

### 15. Caderno de erros ligado às aulas

**Valor para a aluna:** reúne os erros que realmente precisam voltar ao ciclo de estudos.

**Implementação possível:** formulário ou tabela com questão, causa, regra correta, aula e data da nova tentativa.

**Regra própria:** o erro sai do caderno quando a aluna explica a regra e acerta uma nova aplicação.

### 16. Diagnóstico de entrada sem punição

**Valor para a aluna:** ajuda a escolher o ponto inicial sem fazê-la sentir que já deveria saber o conteúdo.

**Implementação possível:** questionário curto sobre disponibilidade, experiência e conhecimentos básicos. O resultado indica rota, não nota.

**Regra própria:** nenhuma pergunta exige conteúdo que o curso ainda não ensinou sem avisar que é apenas diagnóstico.

### 17. Painel de domínio por assunto

**Valor para a aluna:** revela se o problema está em lembrar, comparar ou aplicar.

**Implementação possível:** usar os metadados já presentes nas questões para calcular resultados por aula, tema, dificuldade e tipo de erro.

**Regra própria:** as estatísticas devem gerar uma ação concreta, como revisar uma seção ou refazer um bloco.

### 18. Central de legislação com data de corte

**Valor para a aluna:** facilita conferir a norma vigente e entender o que mudou.

**Implementação possível:** manter links oficiais, artigos exigidos, data de consulta, histórico de mudanças e aulas afetadas.

**Regra própria:** a VX não reproduzirá compilações sem controle. A fonte oficial continuará prevalecendo.

### 19. Flashcards com fila de revisão

**Valor para a aluna:** concentra o esforço nos cartões esquecidos e reduz repetição desnecessária.

**Implementação possível:** começar com marcações “lembrei”, “quase” e “não lembrei”. Depois, usar agendamento local simples.

**Regra própria:** todo cartão terá origem na aula e uma única tarefa.

### 20. Modo de reta final

**Valor para a aluna:** reorganiza o curso quando o tempo até a prova fica curto.

**Implementação possível:** criar uma rota com revisão, legislação, erros e simulados, sem produzir uma segunda versão completa das aulas.

**Regra própria:** prioridades virão do edital, do desempenho da aluna e de análise documentada da FEPESE.

### 21. Áudios curtos de revisão

**Valor para a aluna:** permite revisar em deslocamentos e tarefas leves.

**Implementação possível:** produzir roteiros próprios de cinco a dez minutos a partir dos resumos aprovados.

**Regra própria:** áudio será complemento. Não substituirá a explicação necessária nem exigirá copiar uma aula em vídeo de terceiros.

### 22. Canal de dúvidas com resposta ligada ao conteúdo

**Valor para a aluna:** impede que uma dúvida pequena bloqueie a sequência.

**Implementação possível:** começar de forma assíncrona, com perguntas vinculadas a aula e seção. Perguntas repetidas podem melhorar a própria aula.

**Regra própria:** depende de responsável e prazo de resposta definidos antes da abertura.

## Roadmap priorizado

## Prioridade alta

1. Concluir todas as disciplinas com o padrão do Módulo 1.
2. Criar planos semanais de 5, 10 e 15 horas.
3. Implantar agenda marcável de revisão no dia seguinte, após uma semana e após um mês.
4. Criar caderno de erros ligado a aulas e questões.
5. Criar painel manual de cobertura, progresso e revisões pendentes.
6. Estruturar a central de legislação e o controle de atualizações.
7. Aplicar o padrão de análise da FEPESE a todas as disciplinas.

## Prioridade média

1. Criar diagnóstico de entrada e rotas recomendadas.
2. Transformar o painel manual em estatísticas locais por tema, dificuldade e erro.
3. Implantar fila de revisão dos flashcards.
4. Criar modo de reta final baseado em desempenho e tempo disponível.
5. Ampliar mapas mentais e revisões finais sem duplicar as aulas.
6. Gerar PDF e Word automaticamente a partir da fonte principal.

## Prioridade baixa

1. Produzir áudios curtos de revisão.
2. Abrir canal de dúvidas após definir equipe e prazo de resposta.
3. Avaliar videoaulas somente para assuntos em que a demonstração visual agregue valor claro.
4. Avaliar elementos leves de incentivo, sem transformar estudo em competição vazia.
5. Avaliar encontros de revisão ao vivo quando houver escala e equipe.

## Regra de preservação dos diferenciais

Ao criar um novo recurso, confirme:

- [ ] resolve uma dificuldade real da aluna;
- [ ] mantém a linguagem para iniciantes;
- [ ] leva a uma ação clara;
- [ ] funciona no celular;
- [ ] usa conteúdo e exemplos próprios;
- [ ] preserva fontes e direitos autorais;
- [ ] pode ser mantido pela equipe;
- [ ] não cria uma segunda versão divergente do curso;
- [ ] não atribui comportamento à FEPESE sem evidência;
- [ ] melhora aprendizagem, decisão ou continuidade do estudo.
