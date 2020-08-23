from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

# token
with open("./token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()

# updater 
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

# message handler
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    context.bot.send_message(chat_id=user_id, text=user_text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# polling
updater.start_polling()
