from cgitb import text
from lib2to3.pgen2 import token
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
response = {}

def lambda_handler(event=None, context=None):
  
  for key in site:
    req = requests.get(f'https://{key}')
    if site[key] in req.text:
      response[key] = f'{req.status_code} String Found in {key}'
    else:
      response[key] = f'{req.status_code} Not Found in {key}'

  bot.send_message(text=response , chat_id=-764108168)

  return response

lambda_handler()