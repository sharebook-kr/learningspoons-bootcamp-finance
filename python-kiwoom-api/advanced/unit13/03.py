import telegram
import time

with open("./token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()

bot = telegram.Bot(token)

while True:
    bot.sendMessage(chat_id=389678770, text="안녕하세요. 저는 봇입니다.")
    time.sleep(1)