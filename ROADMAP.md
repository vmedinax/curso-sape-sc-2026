# Roadmap do projeto

Este roadmap organiza a transformação do repositório em uma plataforma editorial profissional. Datas serão definidas depois da confirmação do edital, da equipe e do modelo de acesso.

## Convenções

- `[ ]` não iniciado
- `[-]` em andamento
- `[x]` concluído
- Cada fase somente termina quando todos os seus critérios de saída forem atendidos.

## Fase 0 — Decisões de produto e conformidade

- [ ] Confirmar o concurso, os cargos, a banca e o edital oficial de referência.
- [ ] Definir público-alvo, proposta pedagógica e escopo do curso.
- [ ] Definir licença, termos de acesso e fronteira entre conteúdo público e premium.
- [ ] Definir identidade visual e política de uso de material de terceiros.
- [ ] Designar responsáveis por autoria e revisões.

**Critério de saída:** decisões registradas, fontes oficiais identificadas e responsáveis definidos.

## Fase 1 — Fundação do repositório

- [x] Realizar auditoria técnica inicial.
- [x] Definir regras permanentes e padrão editorial.
- [x] Configurar arquivos básicos do editor e do Git.
- [x] Criar configuração inicial do MkDocs Material.
- [x] Criar navegação estrutural sem conteúdo didático.
- [ ] Definir e adicionar licença.
- [ ] Criar `.gitattributes` e configuração de lint para Markdown.
- [ ] Fixar dependências e gerar arquivo de lock.
- [ ] Aprovar estratégia definitiva de branches.

**Critério de saída:** um clone novo reproduz a estrutura e possui regras técnicas e editoriais inequívocas.

## Fase 2 — Plataforma e automação

- [ ] Configurar integração contínua para lint, links e build estrito.
- [ ] Configurar publicação protegida no GitHub Pages.
- [ ] Automatizar atualização segura de dependências.
- [ ] Criar templates de issue e pull request.
- [ ] Avaliar preview de site para pull requests.

**Critério de saída:** toda alteração é validada e a branch de publicação gera o site automaticamente.

## Fase 3 — Pipeline editorial

- [ ] Transformar o edital oficial em matriz estruturada e rastreável.
- [ ] Criar schemas para aulas, questões, flashcards e simulados.
- [ ] Criar templates correspondentes aos schemas.
- [ ] Definir checklists de revisão técnica, pedagógica, linguística e jurídica.
- [ ] Criar indicadores de cobertura e atualização.

**Critério de saída:** um artefato estrutural percorre o fluxo editorial completo com validação automática.

## Fase 4 — Exportação multiformato

- [ ] Configurar Pandoc para geração de PDF e DOCX.
- [ ] Criar template de PDF e documento de referência do Word.
- [ ] Testar tabelas, imagens, notas, equações, links e caracteres portugueses.
- [ ] Incorporar versão, data e hash do commit aos artefatos.
- [ ] Publicar exportações como artefatos ou assets de release.

**Critério de saída:** site, PDF e DOCX são reproduzíveis a partir do mesmo Markdown aprovado.

## Fase 5 — Produção e qualidade didática

- [ ] Autorizar o início da produção após aprovação das fases anteriores.
- [ ] Priorizar unidades pela matriz do edital.
- [ ] Submeter cada unidade às revisões obrigatórias.
- [ ] Vincular unidades, revisões e exercícios aos itens do edital.
- [ ] Eliminar lacunas antes da primeira edição completa.

**Critério de saída:** cobertura planejada integral, rastreável e aprovada.

## Fase 6 — Lançamento e operação contínua

- [ ] Definir versionamento e calendário de releases.
- [ ] Publicar site e materiais de distribuição.
- [ ] Manter erratas e changelog.
- [ ] Monitorar atualizações normativas e links externos.
- [ ] Estabelecer processo de feedback com privacidade adequada.

**Critério de saída:** publicação reproduzível e rotina de manutenção documentada.

## Fora do escopo neste momento

- criação de aulas, questões, flashcards ou simulados;
- definição unilateral do conteúdo do edital;
- publicação automática;
- geração e versionamento de PDF, DOCX ou ZIP;
- contratação de serviços ou inclusão de ferramentas sem avaliação.
