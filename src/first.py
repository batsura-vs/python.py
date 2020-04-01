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


class score:
    score = 0


class maths:
    d: int
    f: int
    g: int
    k: int


class help:
    name: str
    surName: str
    Born: datetime


def randomPlas(phase, update):
    if phase >= 3:
        update.message.reply_text('ну а теперь', help.name, 'займёмся математикой')
        while phase < 30:
            d = random.randrange(1, 1)
        if d == 1:
            a = random.randrange(1, 200)
            b = random.randrange(1, 200)
            c = a + b
            update.message.reply_text(a, '+', b, '=')
            maths.d = update.message.text
            if maths.d == c:
                score.score = score.score + 1
                update.message.reply_text('молодец твой счет =', score.score)
                phase += 1
            else:
                update.message.reply_text('неверно')
                update.message.reply_text(a, '+', b, '=',c)


def hi(phase, update):
    logger.info('hi ' + str(phase.phase))
    if phase.phase == 0:
        update.message.reply_text('привет, как тебя зовут?')
        help.name = update.message.text
        phase.phase += 1
        return True
    else:
        return False


def surname(phase, update):
    logger.info('surname' + str(phase.phase))
    if phase.phase == 1:
        update.message.reply_text('а какая фамилия у тебя?')
        help.surName = update.message.text
        phase.phase += 1
        return True
    else:
        return False


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def born(phase, update):
    logger.info('born' + str(phase.phase))
    if phase.phase == 2:
        try:
            update.message.reply_text('твой год рождения в формате дд.мм.гггг')
            help.Born = datetime.strptime(update.message.text, '%d.%m.%Y')
            phase.phase += 1
            return True
        except ValueError:
            return False


masiv = [hi, born, surname,randomPlas]
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
