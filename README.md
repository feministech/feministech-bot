# Feministech Bot ✨

> ❓ Este é nosso bot disponível em todos os chats dos canais de pessoas streamers da comunidade Feministech, foi feito em Python, utilizando o gerenciador de ambientes Poetry, a biblioteca TwitchIO, as ferramentas de qualidade de código blue e isort, com automações utilizando taskipy, e totalmente documentado com Mkdocs.

---

## 📋 Requisitos

### 🤖 Produção:

- [Python (^3.11)](https://www.python.org/)
- [TwitchIO (^2.6.0)](https://twitchio.dev/)

### 🧰 Desenvolvimento:

- [Poetry (^1.4.2)](https://python-poetry.org/)
- [Blue (^0.9.1)](https://blue.readthedocs.io/en/latest/)
- [iSort (^5.12.0)](https://pycqa.github.io/isort/)
- [TaskiPy (^1.10.4)](https://github.com/taskipy/taskipy)

### 📚 Documentação:

- [Mkdocs-material (^9.1.5)](https://squidfunk.github.io/mkdocs-material/)
- [Mkdcostrings (^0.20.0)](https://mkdocstrings.github.io/)
- [Mkdocstrings-python (^0.9.0)](https://mkdocstrings.github.io/python/)
- [Termynal (^0.2.1)](https://daxartio.github.io/termynal/)

---

## 🔎 Como utilizar

Para utilizar ou trabalhar tanto no bot, quanto na documentação é necessário rodar o comando abaixo no seu terminal, dentro da pasta do projeto na sua máquina:

```console
$ poetry install
```

### 🤖 Bot:

Para utilizar o bot, basta seguir os próximos passos:

- Configure o arquivo `config.ini`.

> 📚 Para mais informações sobre esse arquivo, acesse a nossa documentação [clicando aqui](https://feministech.github.io/feministech-bot/configuracao.md).

- Execute o bot:

```console
poetry run bot
```

_⚠️ É necessário desligar o bot com as teclas de atalho CTRL + C e rodá-lo novamente com o comando acima, a cada alteração feita em seu código._

> 📚 Para mais informações de como configurar o seu ambiente Python com Poetry, acesse a nossa documentação [clicando aqui](https://feministech.github.io/feministech-bot/ambiente).

### 📚 Documentação:

Para trabalhar na documentação, basta editar os arquivos markdown (`.md`) dentro da pasta `docs`.

Caso precise adicionar imagens ou outros conteúdos de mídia na documentação, por padrão, deixe-os na pasta `docs/assets`.

Ou para alterações e melhorias no estilo, basta editar o arquivo `extra.css`, dentro da pasta `docs/stylesheets`.

Para visualizar as alterações feitas na documentação na sua máquina, basta rodar o comando e acessar pelo endereço informado na última linha:

```console
poetry run task docs
```

---

## 📋 Issues

Fique à vontade para abrir uma issue caso encontre algum bug ou tenha alguma sugestão, assim podemos discutir o melhor caminho para melhorá-la ou corrigi-lá.

---

## 👋 Contribuição

Você será sempre bem-vinde a contribuir com este projeto, pedimos apenas que preze pela qualidade de código, seguindo a estrutura e organização planejada nele.

Ao finalizar o trabalho, não deixe de rodar as nossas ferramentas de qualidade de código, com o comando abaixo:

```console
poetry run task lint
```

Finalizados os trabalhos, basta criar sua pull request e aguardar a revisão.

> 💡 Aproveite e confira nas nossas issues, se existe alguma prioridade ou sugestão de contribuição.

---

## 📎 Links

- [Site oficial da Feministech](https://feministech.com.br/)
- [Site do Time Feministech na Twitch](https://www.twitch.tv/team/livecodergirls)
- [Documentação Oficial do Bot](https://feministech.github.io/feministech-bot/)

---

## 📜 Licença

Este projeto é feito sobre a licença GNU, para mais informações sobre a sua possível utilização, modificação e compartilhamento, [clique aqui](https://github.com/feministech/feministech-bot/blob/main/LICENSE).

---

<p align=center>Feito com ❤️ pela <a href="https://feministech.com.br/" target="blank_">comunidade Feministech.</a></p>
