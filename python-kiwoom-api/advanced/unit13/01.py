import telegram

with open("./token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()

bot = telegram.Bot(token)
updates = bot.getUpdates()

for i in updates:
    print(i.message)
