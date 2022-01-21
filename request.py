import logging
import requests
import json
import telegram

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bot = telegram.Bot(token='1976234351:AAEWwn6acG3iJsZzTrRC5JBrmZ9xGfBmieY')
site = {
  'surabaya.go.id': '<div class="teks-surabaya-2">Gotong Royong Menuju Surabaya Kota Dunia<br>yang Maju, Humanis, Dan Berkelanjutan</div>',
  'esurat.surabaya.go.id': '<h4>Log In eSurat</h4>',
  'sswalfa.surabaya.go.id': '<h2 class="text-white text-center font-weight-bold">Ajukan Permohonan Izin Melalui SSW</h2>',
}

def lambda_handler(event=None, context=None):

  response = ''
  
  for key in site:
    req = requests.get(f'https://{key}')
    if site[key] in req.text:
      response += f'{req.status_code} String Found in {key}\n'
    else:
      response += f'{req.status_code} Not Found in {key}\n'

  bot.send_message(text=response , chat_id=-764108168)
  print(response)

lambda_handler()