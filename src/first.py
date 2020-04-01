from dataclasses import dataclass
from random import random
from enum import Enum, auto
from datetime import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@dataclass()
class phase:
    phase = 0
class phase2:
    phase2 = 0
class help:
    name:str
    surName:str
    Born: datetime

def random(phase2,update):
    d=random.randrange(1,4)
    if d == 1:
        update.message.reply_text('ну а теперь',)


def hi(phase, update):
    logger.info('hi ' + str(phase.phase))
    if phase.phase == 0:
        update.message.reply_text('привет, как тебя зовут?')
        help.name=update.message.text
        phase.phase += 1
        return True
    else:
        return False


def surname(phase, update):
    logger.info('surname'+str(phase.phase))
    if phase.phase == 1:
        update.message.reply_text('а какая фамилия у тебя?')
        help.surName=update.message.text
        phase.phase += 1
        return True
    else:
        return False


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def born(phase, update,phase2):
    logger.info('born'+ str(phase.phase))
    if phase.phase == 2:
        try:
            update.message.reply_text('твой год рождения в формате дд.мм.гггг')
            help.Born = update.message.text
            rod = datetime.strptime(update.message.text, '%d.%m.%Y')
            phase.phase += 1
            phase2.phase2 += 1
            return True
        except ValueError:
            return False


masiv = [hi, born, surname]
phase.phase = 0


def sborka(update, context):
    for handler in masiv:
        if handler(phase, update) is True:
            return


def main():
    updater = Updater("1060586927:AAEJMxZGceoJglzSPEx4-Sm1y-RupIYddPw", use_context=True)
    dp = updater.dispatcher
    super_hendler = MessageHandler(Filters.text, sborka)
    dp.add_handler(super_hendler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
