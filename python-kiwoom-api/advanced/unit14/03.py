from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import requests 
from bs4 import BeautifulSoup

# token
with open("./token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()

# updater 
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def get_dividiend(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_dvr")
    dividend = tags[0].text
    return dividend

# message handler
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    dividend = get_dividiend(user_text)
    text = f"배당수익률: {dividend}"
    context.bot.send_message(chat_id=user_id, text=text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# polling
updater.start_polling()
