from dataclasses import dataclass
import random
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


class chekio:
    check: int


chekio.check = 0


class ansver:
    c: int
    a: int
    b: int


class randMove:
    d = random.randrange(1, 1)


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


def startMaths(phase, update):
    help.Born = datetime.strptime(update.message.text, '%d.%m.%Y')
    if phase.phase == 3:
        if randMove.d == 1:
            ansver.a = random.randrange(1, 200)
            ansver.b = random.randrange(1, 200)
            ansver.c = ansver.a + ansver.b
            update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', ansver.a, '+', ansver.b,
                                      '=')
            chekio.check = 1
        if randMove.d == 2:
            ansver.a = random.randrange(100, 200)
            ansver.b = random.randrange(1, 100)
            ansver.c = ansver.a - ansver.b
            update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', ansver.a, '-', ansver.b,
                                      '=')
            chekio.check = 2
        if randMove.d == 3:
            while ansver.a % ansver.b != 0:
                ansver.a = random.randrange(100, 200)
                ansver.b = random.randrange(1, 100)
                ansver.c = ansver.a / ansver.b
                update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', ansver.a, ':',
                                          ansver.b, '=')
                chekio.check = 3
        if randMove.d == 4:
            ansver.a = random.randrange(1, 10)
            ansver.b = random.randrange(1, 15)
            ansver.c = ansver.a * ansver.b
            update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', ansver.a, '*', ansver.b,
                                      '=')
            chekio.check = 4


def plas(phase, update):
    if chekio.check == 1:
        if randMove.d == 1:
            update.message.reply_text('молодец')
            chekio.check = 0
    else:
        update.message.reply_text('неверно \n', ansver.a, '+', ansver.b, '=', ansver.c)
        chekio.check = 0


def chek(phase, update):
    if chekio.check == 1:
        maths.d = update.message.text
        if maths.d == ansver.c:
            update.message.reply_text('молодец')
            chekio.check = 0
        else:
            update.message.reply_text('лапух!!!')
            chekio.check = 0


def hi(phase, update):
    logger.info('hi ' + str(phase.phase))
    if phase.phase == 0:
        update.message.reply_text('привет, как тебя зовут?')
        phase.phase += 1
        return True
    else:
        return False


def surname(phase, update):
    logger.info('surname' + str(phase.phase))
    if phase.phase == 1:
        update.message.reply_text('а какая фамилия у тебя?')
        help.name = update.message.text
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
            help.surName = update.message.text
            phase.phase += 1
            return True
        except ValueError:
            return False


masiv = [hi, born, surname, startMaths]
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
