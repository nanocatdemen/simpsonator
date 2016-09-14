from flask import Flask, request, Response
import requests
from config import bot_token, ip

app = Flask(__name__)

telegram_url = 'https://api.telegram.org/bot' + bot_token + '/'

method_names = { 'set_webhook': 'setWebhook' }
methods = { k: telegram_url + method for k, method in method_names.items() }

# remove webhook if exists
r = requests.post(methods['set_webhook'])
# set webhook
r = requests.post(methods['set_webhook'], data = {'url': ip})

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        print(request)
        print(request.args)
        print(request.charset)
        return Response()
