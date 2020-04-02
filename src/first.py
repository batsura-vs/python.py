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
class Phase:
    phase = 0
    randMove = 1
    c = 0
    a = 0
    b = 0


class help:
    name: str
    surName: str
    Born: datetime


def startMaths(phase, update):
    if phase.phase == 3:
        logger.info("startMath start")
        help.Born = datetime.strptime(update.message.text, '%d.%m.%Y')
        if phase.randMove == 1:
            phase.a = random.randrange(1, 200)
            phase.b = random.randrange(1, 200)
            phase.c = phase.a + phase.b
            update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', phase.a, '+', phase.b,
                                      '=')
            chekio.check = 1
        '''if phase.randMove == 2:
            phase.a = random.randrange(100, 200)
            phase.b = random.randrange(1, 100)
            phase.c = phase.a - phase.b
            update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', phase.a, '-', phase.b,
                                      '=')
            chekio.check = 2
        if phase.randMove == 3:
            while phase.a % phase.b != 0:
                phase.a = random.randrange(100, 200)
                phase.b = random.randrange(1, 100)
                phase.c = phase.a / phase.b
                update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', phase.a, ':',
                                          phase.b, '=')
                chekio.check = 3
        if phase.randMove == 4:
            phase.a = random.randrange(1, 10)
            phase.b = random.randrange(1, 15)
            phase.c = phase.a * phase.b
            update.message.reply_text('ну а теперь ' + help.name + ' займёмся математикой \n ', phase.a, '*', phase.b,
                                      '=')
            chekio.check = 4'''


def plas(phase, update):
    if chekio.check == 1:
        if phase.randMove == 1:
            update.message.reply_text('молодец')
            chekio.check = 0
    else:
        update.message.reply_text('неверно \n', phase.a, '+', phase.b, '=', phase.c)
        chekio.check = 0


def chek(phase, update):
    if chekio.check == 1:
        maths.d = update.message.text
        if maths.d == phase.c:
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
            phase.phase += 1
            return True
        except ValueError:
            return False


def getUserContext(update):
    key = update.message.chat.username
    userData = users.get(key)
    if userData is None:
        userData = Phase()
        users[key] = userData
    return userData


users = {}
masiv = [hi, born, surname]


def sborka(update, context):
    phase = getUserContext(update)
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
