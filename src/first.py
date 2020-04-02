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
    randMove = 0
    c = 0
    a = 0
    b = 0
    name = None
    surName = None
    born = None
    check = None
    d = None


def startMaths(phase, update):
    if phase.phase == 3:
        logger.info("startMath start")
        phase.Born = datetime.strptime(update.message.text, '%d.%m.%Y')
        logger.info("startMath start2")
        logger.info("startMath start3")
        phase.a = random.randrange(1, 200)
        phase.b = random.randrange(1, 200)
        phase.c = phase.a + phase.b
        update.message.reply_text(
            'ну а теперь ' + phase.name + ' займёмся математикой \n' + str(phase.a) + '+' + str(phase.b) +
            '=')
        phase.check = 1


def plas(phase, update):
    if phase.randMove != 1:
        return False
        phase.a = random.randrange(1, 200)
        phase.b = random.randrange(1, 200)
        phase.c = phase.a + phase.b
        update.message.reply_text(str(a) + '+' + str(b) + '=')
        phase.check = 1


def plasCheck(phase, update):
    if phase.check != 1:
        return False
    else:
        d = update.message.text
        if phase.c == int(d):
            update.message.reply_text('молодец')
            phase.check = 0
            phase.randMove = random.randrange(1, 4)
            return True
        if phase.c != int(d):
            update.message.reply_text('неверно \n' + str(phase.a) + '+' + str(phase.b) + '=' + str(phase.c))
            phase.check=0
            phase.randMove = random.randrange(1, 4)
            return True

def minCheck(phase,update):
    if phase.check != 2:
        return False
    else:
        d = update.message.text
        if phase.c == int(d):
            update.message.reply_text('молодец\n' + str(phase.a) + '-' + str(phase.b) + '=' + str(phase.c))
            phase.check = 0
            phase.randMove = random.randrange(1, 4)
            return True
        if phase.c != int(d):
            update.message.reply_text('неверно \n' + str(phase.a) + '-' + str(phase.b) + '=' + str(phase.c))
            phase.check = 0
            phase.randMove = random.randrange(1, 4)
            return True


def delenchek(phase, update):
    if phase.phase != 6:
        return False
    else:
        d = update.message.text
        if phase.c == int(d):
            update.message.reply_text('молодец')
            phase.check = 0
            return True
        if phase.c != int(d):
            update.message.reply_text('неверно \n' + str(phase.a) + ':' + str(phase.b) + '=' + str(phase.c))


def hi(phase, update):
    logger.info('hi ' + str(phase.phase))
    if phase.phase == 0:
        update.message.reply_text('привет, как тебя зовут?')
        phase.phase += 1
        return True
    else:
        return False


def surname(phase, update):
    if phase.phase != 1:
        return False
    logger.info('surname' + str(phase.phase))
    update.message.reply_text('а какая фамилия у тебя?')
    phase.name = update.message.text
    phase.phase += 1
    return True


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
masiv = [hi, born, surname, startMaths, plas]


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
