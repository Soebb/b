#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]

import logging
from yun import Yun
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import constants
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(constants.welcome_text)


def shortlink(update: Update, context: CallbackContext) -> None:
    api = Yun('509:66zjkr6vbw08csog80swgccgow8owwc')
    result = api.short('title', 'url')
    update.message.reply_text(result)




def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    ocr_bot_token=os.environ.get("BOT_TOKEN", "")
    updater = Updater(ocr_bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(filters.regex(r'https?://[^\s]+'), shortlink))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
