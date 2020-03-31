from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
import logging
from telegram import update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def mesto(phase):
    phase = 0


# создаём функцию хай
def hi(phase):
    if phase == 0:
        # создаём переменную d и присваиваем ей значениу типа str
        d = 'привет, как тебя зовут?'
        h=update.massege.text
        phase += 1
        return True
    else:
        return False


# создаём функцию фамилия


def surname(phase):
    if phase == 1:
        d = 'а какая фамилия у тебя?'
        h=update.messege.text
        phase+=1
        return True
    else:
        return False

def sborka(surname,hi):
    update.message.reply_text(hi,surname)


def main():
    updater = Updater("1060586927:AAEJMxZGceoJglzSPEx4-Sm1y-RupIYddPw", use_context=True)
    dp = updater.dispatcher
    dp.add_error_handler(error)
    dp.add_sborka_hendler(surname(),hi())
    updater.start_polling()
    updater.idle()
