# Configuração das credenciais ⚙️

Para que o bot possa funcionar, você deve criar um arquivo `config.ini`, onde ficarão todas as suas credenciais.

```ini
[config]
token = xxxxx
username = xxxxx
channels = xxxxx xxxxx xxxxx
bots = xxxxx xxxxx xxxxx
project = xxxxx
```

> 💡 Você pode usar como exemplo o arquivo `exemplo_config.ini` como base para o seu. Basta substituir os os campos `xxxxx` por suas credenciais.

## ❓ O que é cada chave?

Caso você seja uma pessoa nova no mundo dos bots e das lives, aqui fica um exemplo do que cada valor siginifica:

| Chave | Valor | Exemplo |
| ----- | ----- | ------- |
| token    | [gerador de token da twitch](https://twitchapps.com/tmi/)  | oauth:***** |
| username | nome do seu canal | feministech |
| channels | nome dos canais onde o bot rodará | feministech bug_elseif |
| bots     | outros bots que não responderão aos eventos | steamlabs streamelements |
| project  | nome de um projeto que queira divulgar | time de streamers |

> ⚠️ No caso da chave channels e bots, quando mais de um valor, deve-se separá-los com um espaço em branco.