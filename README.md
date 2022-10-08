# Feministech bot

Bot da Feministech para Twitch


---


## Instalação do bot

Esse bot é feito em [Python](python.org) e usa o genrenciador de ambientes [Poetry](https://python-poetry.org/)

Caso tenha dificuldades em instalar o Python e o Poetry [Clique aqui!](/docs/instalacao.md)


## Como executar o bot?

### Instalação das bibliotecas

Para executar o bot, primeiro você precisa instalar as bibliotecas necessárias. O Poetry pode te ajudar com isso. Você deve navegar no terminal até o diretório do seu projeto e executar:

```bash
poetry install
```

Após diversas linhas de resposta no termnal, você deve ver a ultima linha:

```bash
Installing the current project: botlive (0.1.0)
```

Isso siginifica que os pacotes do bot foram instalados e agora ele pode executado

### Configuração das credenciais

Para que o bot possa funcionar no chat da sua live, você deve criar um arquivo `config.ini`. Onde ficarão todas as suas credenciais.

```ini
[config]
token = 'xxxxxxxxxx'
username = 'xxxxxxxxxx'
bots = 'xxxxxxxxxx'
project = 'xxxxxxxxxx'
```

Você pode usar como exemplo o arquivo `exemplo_config.ini` como base para o seu. Basta substituir os os campos `xxxxxxxxxx` por suas credenciais.

#### O que é cada chave?

Caso você seja uma pessoa nova no mundo dos bots e das lives, aqui fica um exemplo do que cada valor siginifica:

| Chave | Valor | Exemplo |
| ----- | ----- | ------- |
| token    |       |         |
| username |       |         |
| bots     |       |         |
| project  |       |         |

### Execução do bot

O pacote do bot, quando instalado com sucesso, tem um comando do Poetry para iniciar o bot:

```bash
poetry run botlive
```
