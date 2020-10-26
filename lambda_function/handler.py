from botocore.vendored import requests
import logging
import config 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TELEGRAM_TOKEN = config.TELEGRAM_TOKEN
BOT_URL = "https://api.telegram.org/bot{}/".format(TELEGRAM_TOKEN)

def create_response(text):
    return "Hey there, you wrote " + text

def send_text_message(text, chat_id):
    url = BOT_URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def lambda_handler(event, context):
    logger.info(event)
    chat_id = event['message']['chat']['id']
    text = event['message']['text']
    response = create_response(text)
    send_text_message(response, chat_id)
    return {
        'statusCode': 200
    }

