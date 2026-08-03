# Como contribuir

Obrigado por contribuir com o Curso SAPE/SC 2026. O projeto está em fundação e ainda não aceita produção didática sem autorização explícita.

## Antes de começar

1. Leia `AGENTS.md`, `README.md`, `STYLE_GUIDE.md` e `ROADMAP.md`.
2. Confirme se a alteração pertence à fase atual.
3. Verifique o estado do Git e preserve mudanças que já estejam no diretório de trabalho.
4. Para alterações amplas ou decisões editoriais, abra uma discussão ou issue antes de implementar.

## Escopo atual

São aceitas melhorias de estrutura, documentação, acessibilidade, validação e automação previamente aprovadas. Não crie aulas, questões, flashcards ou simulados até que edital, templates, schemas e fluxo de revisão estejam aprovados.

## Branches e commits

- `main` deve permanecer publicável.
- Enquanto `develop` existir, use-a como branch de integração e publique somente após aprovação em `main`.
- Crie branches curtas com nomes como `docs/...`, `chore/...`, `fix/...` ou, futuramente, `content/...`.
- Faça commits pequenos e com uma finalidade clara.
- Prefira mensagens no imperativo, por exemplo: `docs: define padrão editorial`.
- Não faça force push, reescrita de histórico ou commit de artefatos gerados.

## Alterações editoriais futuras

Toda unidade didática deverá:

- seguir `STYLE_GUIDE.md`;
- usar metadados válidos e identificador único;
- indicar os itens correspondentes do edital;
- citar fontes primárias e registrar data de consulta quando necessário;
- respeitar direitos autorais e licenças;
- passar por revisão técnica, pedagógica, linguística e de fontes;
- compilar sem avisos no site e nos formatos aplicáveis.

## Pull requests

Um pull request deve explicar:

- problema ou objetivo;
- arquivos e comportamento afetados;
- decisões e limitações relevantes;
- verificações executadas;
- fontes e permissões, quando houver conteúdo externo.

Evite misturar reorganização, conteúdo e formatação em uma única mudança. Não aprove conteúdo próprio quando houver outro revisor disponível.

## Validação local

Quando MkDocs Material estiver instalado, execute:

```powershell
mkdocs build --strict
```

Também revise o diff, confirme que links são relativos e verifique que nenhum arquivo gerado, segredo ou dado pessoal foi incluído.

## Arquivos gerados e dependências

- Não versione `site/`, `build/`, PDF, DOCX, ZIP, caches ou ambientes virtuais.
- Não edite manualmente uma saída gerada.
- Dependências novas precisam de justificativa, versão fixada e avaliação de manutenção/licença.

## Segurança e conformidade

Não publique credenciais ou vulnerabilidades exploráveis em issues públicas. Não inclua material protegido, dados pessoais ou informação sem fonte verificável. Se houver dúvida sobre permissão de uso, interrompa a inclusão até a análise responsável.
