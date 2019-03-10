from core.models import Interaction
from core.constants import TOKEN
import requests


def proccess(json_telegram):
    user_id = json_telegram['message']['chat']['id']
    command = json_telegram['message']['text']
    interaction = Interaction.objects.get(input=command, active=True)

    send(user_id, interaction.output)


def send(chat_id, output):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': output}
    requests.post(url, data=data)
