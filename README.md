Bot criado para o [**grupy de araraquara do telegram**](https://t.me/grupyaqa).



## Instalação:
 
git clone git@github.com:rafaelsevla/grupybot.git

## Crie uma virtualenv, ative-a e instale os pacotes

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

Faça as migrates necessárias do projeto e crie um super usuário para seu painel administrativo com os comandos
```
python manage.py migrate
python manage.py createsuperuser
```

## Modo de uso:
Adicione o token do seu bot no arquivo [**constants**](https://github.com/rafaelsevla/grupybot/blob/master/core/constants.py)

Com um servidor rodando a aplicação (pode ser ngrok, por exemplo), ative o seu bot acessando o link do servidor com path events com o token do seu bot
```
https://api.telegram.org/bot<token>/setWebhook?url=https://9a2c2955.ngrok.io/events/
```

E enfim na sua página administrativa
``` https://9a2c2955.ngrok.io/admin/ ``` crie os comandos de input e output para o bot na aba de Interactions.

