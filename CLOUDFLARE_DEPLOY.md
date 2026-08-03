# Publicação protegida no Cloudflare Pages

Este projeto usa MkDocs Material para gerar o site e Cloudflare Pages Functions para proteger todas as páginas com autenticação HTTP Basic.

As credenciais não ficam no GitHub. Elas devem ser cadastradas como segredos criptografados no painel do Cloudflare.

## Antes de começar

Confirme que:

- o repositório está privado no GitHub;
- a branch de produção é `main`;
- `requirements.txt`, `mkdocs.yml` e `functions/_middleware.js` estão versionados;
- nenhuma credencial real está em arquivo do repositório.

## Conectar o GitHub ao Cloudflare Pages

1. Entre no painel do Cloudflare.
2. Abra **Workers & Pages**.
3. Selecione **Create application** e a opção para conectar um repositório Git.
4. Escolha **Pages**, quando essa escolha for exibida.
5. Conecte sua conta do GitHub.
6. Na autorização do aplicativo Cloudflare Pages no GitHub, permita acesso apenas ao repositório `curso-sape-sc-2026`.
7. Selecione o repositório privado `curso-sape-sc-2026`.
8. Use `curso-sape-sc-2026` como nome do projeto, se o nome estiver disponível.
9. Selecione `main` como branch de produção.

O acesso concedido ao aplicativo do Cloudflare permite que o serviço faça o build. Ele não torna o repositório público.

## Configurar o build

Preencha os campos da implantação com estes valores exatos:

| Campo | Valor |
|---|---|
| Framework preset | `None` |
| Production branch | `main` |
| Root directory | `/` ou deixe vazio |
| Build command | `python -m pip install --requirement requirements.txt && python -m mkdocs build --strict` |
| Build output directory | `site` |

Em **Settings > Variables and Secrets**, adicione também esta variável de build:

| Nome | Valor | Tipo |
|---|---|---|
| `PYTHON_VERSION` | `3.13` | texto simples |

`PYTHON_VERSION` não é uma credencial. Ela apenas fixa a versão do Python usada no build.

## Cadastrar as credenciais como secrets

No projeto do Cloudflare Pages:

1. Abra **Settings > Variables and Secrets**.
2. Selecione o ambiente **Production**.
3. Adicione `COURSE_USERNAME`.
4. Digite o usuário escolhido e marque **Encrypt**.
5. Adicione `COURSE_PASSWORD`.
6. Digite uma senha longa e exclusiva e marque **Encrypt**.
7. Salve as duas configurações.
8. Repita o cadastro no ambiente **Preview** se as URLs de pré-visualização também forem usadas.
9. Inicie uma nova implantação depois de cadastrar ou alterar os secrets.

Use de preferência letras ASCII no usuário e na senha. Evite espaços, acentos e dois-pontos no nome de usuário. A senha pode conter dois-pontos.

Nunca coloque os valores de `COURSE_USERNAME` ou `COURSE_PASSWORD` no `mkdocs.yml`, no código, no histórico do Git ou nas mensagens de commit.

## Fazer a primeira implantação

Após salvar a configuração, inicie a implantação. O Cloudflare deverá:

1. clonar o repositório privado;
2. instalar as versões fixadas em `requirements.txt`;
3. executar `mkdocs build --strict`;
4. publicar o conteúdo da pasta `site`;
5. detectar e implantar `functions/_middleware.js` como Pages Function.

Se o nome sugerido estiver disponível, o endereço será:

```text
https://curso-sape-sc-2026.pages.dev
```

## Testar a proteção

Faça os seguintes testes em uma janela anônima do navegador:

1. Abra a página inicial. O navegador deve solicitar usuário e senha.
2. Cancele a solicitação. A resposta deve ser `401 Unauthorized`.
3. Informe uma senha incorreta. O acesso deve continuar bloqueado.
4. Informe as credenciais corretas. A página deve abrir.
5. Abra diretamente o endereço de uma aula ou de um arquivo estático. A autenticação também deve ser exigida.
6. Teste a URL de preview, caso previews estejam habilitados.

Para conferir o cabeçalho sem enviar credenciais:

```powershell
curl.exe -I https://curso-sape-sc-2026.pages.dev/
```

A resposta esperada contém:

```text
HTTP/2 401
WWW-Authenticate: Basic realm="Curso SAPE/SC", charset="UTF-8"
```

Para testar credenciais corretas sem gravá-las no comando ou no histórico, prefira o navegador. Não inclua a senha em exemplos, capturas de tela ou logs.

## Atualizações automáticas

Com a integração Git habilitada, cada novo commit enviado para `main` inicia automaticamente um build de produção. O site só é atualizado se `mkdocs build --strict` terminar sem erro.

Branches diferentes de `main` podem gerar deployments de preview. Se não precisar deles, abra **Settings > Builds > Branch control** e desative os builds de preview. Isso reduz a quantidade de endereços que precisam ser testados e protegidos.

## Trocar ou revogar a senha

1. Abra **Settings > Variables and Secrets**.
2. Substitua `COURSE_PASSWORD` por um novo valor criptografado.
3. Salve.
4. Faça uma nova implantação para aplicar a alteração.
5. Teste novamente em uma janela anônima.

HTTP Basic não oferece uma tela própria de encerramento de sessão. O navegador pode manter as credenciais durante a sessão. Para revogar o acesso, troque o secret e faça uma nova implantação.

## Teste local opcional

Para testar Pages Functions localmente, instale Node.js e execute o Wrangler pelo `npx`. Crie um arquivo local `.dev.vars` na raiz, sem versioná-lo:

```dotenv
COURSE_USERNAME=usuario-local
COURSE_PASSWORD=senha-local
```

Depois, gere o site e inicie o servidor local:

```powershell
python -m pip install --requirement requirements.txt
python -m mkdocs build --strict
npx wrangler pages dev site
```

O `.gitignore` impede o versionamento de `.dev.vars` e arquivos `.env`.

## Observações de segurança

- Use apenas o endereço HTTPS fornecido pelo Cloudflare ou um domínio personalizado com HTTPS ativo.
- Não compartilhe credenciais por repositórios, issues, commits ou logs.
- A autenticação protege o acesso pela web. Quem recebe acesso ainda pode salvar ou copiar o material exibido no próprio dispositivo.
- Todas as requisições passam pela Function. Elas contam para a franquia gratuita de Workers do Cloudflare.
