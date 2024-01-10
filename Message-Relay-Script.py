import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import os
PORT = int(os.environ.get('PORT', 5000))

# Bot token goes here
TOKEN = ''

# Channel name goes here
CHANNEL_NAME = '@'

# Authorized user IDs go here. Use this to limit who can forward pictures to the bot.
AUTHORIZED_USERS = []

def forward_photo(update, context):
    user_id = update.effective_user.id
    if user_id in AUTHORIZED_USERS:
        photo = update.message.photo[-1].file_id
        context.bot.send_photo(chat_id=CHANNEL_NAME, photo=photo)
        confirmation_message = "\U0001F44D Photo correctly posted!"
        context.bot.send_message(chat_id=update.message.chat_id, text=confirmation_message)
    if user_id not in AUTHORIZED_USERS:
        failure ="\u274C You're not an authorized user!"
        context.bot.send_message(chat_id=update.message.chat_id, text=failure)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.photo, forward_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
