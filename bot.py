import logging
import os
import requests
from yun import Yun
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
)
from telegram.ext.filters import Filters
from telegram.update import Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

token = os.environ.get('BOT_TOKEN')
updater = Updater(token)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hi !  I'm a link shortener bot"
    )

def shortlink(update: Update, context: CallbackContext):
    api = Yun('509:66zjkr6vbw08csog80swgccgow8owwc')
    result = api.short('title', 'url')
    update.message.reply_text(" :لینک شما " + str(result))


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.regex(r'https?://[^\s]+'), shortlink))

updater.start_polling()
updater.idle()
