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
    g = None
    h = None


def startMaths(phase, update):
    if phase.phase == 2:
        phase.phase += 1
        Phase.surName=update.message.text
        logger.info("startMath start")
        phase.a = random.randrange(1, 200)
        phase.b = random.randrange(1, 200)
        phase.c = phase.a + phase.b
        update.message.reply_text(
               'ну а теперь ' + phase.name + ' займёмся математикой \n' + str(phase.a) + '+' + str(phase.b) +
           '=')
        phase.check = 1
        return True


def delen(phase, update):
    if phase.randMove != 3:
        return False
    logger.info("delen start")
    while phase.a % phase.b != 0:
        phase.a = random.randrange(1, 200)
        phase.b = random.randrange(1, 20)
        phase.c = phase.a // phase.b
    update.message.reply_text(str(phase.a) + ':' + str(phase.b) + '=')
    phase.randMove=0
    phase.check = 3
    return True


def umno(phase, update):
    if phase.randMove != 4:
        return False
    logger.info("umno start")
    phase.a = random.randrange(1, 20)
    phase.b = random.randrange(1, 20)
    phase.c = phase.a * phase.b
    update.message.reply_text(str(phase.a) + '*' + str(phase.b) + '=')
    phase.randMove=0
    phase.check = 4
    return True


def min(phase, update):
    if phase.randMove != 2:
        return False
    logger.info("min start")
    phase.a = random.randrange(100, 200)
    phase.b = random.randrange(1, 100)
    phase.c = phase.a - phase.b
    update.message.reply_text(str(phase.a) + '-' + str(phase.b) + '=')
    phase.randMove=0
    phase.check = 2
    return True


def plas(phase, update):
    if phase.randMove != 1:
        return False
    logger.info("plas start")
    phase.a = random.randrange(1, 200)
    phase.b = random.randrange(1, 200)
    phase.c = phase.a + phase.b
    update.message.reply_text(str(phase.a) + '+' + str(phase.b) + '=')
    phase.randMove=0
    phase.check = 1
    return True


def plasCheck(phase, update):
    if phase.check != 1:
        return False
    else:
        logger.info("plasCheck start")
        d = update.message.text
        if phase.c == int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text(phase.name+' молодец напиши класс 1 продолжить \n' + str(phase.a) + '+' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.g +=1
            return True
        if phase.c != int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text('неверно '+phase.surName+'  напиши 1 чтобы продолжить\n' + str(phase.a) + '+' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.h += 1
            return True


def minCheck(phase, update):
    if phase.check != 2:
        return False
    else:
        d = update.message.text
        logger.info("minCheck start")
        if phase.c == int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text(phase.name+' молодец напиши 1 чтобы продолжить\n' + str(phase.a) + '-' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.g +=1
            return True
        if phase.c != int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text('неверно '+phase.name+' напиши 1 чтобы продолжить\n' + str(phase.a) + '-' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.h += 1
            return True


def delenChek(phase, update):
    if phase.check != 3:
        return False
    else:
        d = update.message.text
        logger.info("delenCheck start")
        if phase.c == int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text('молодец '+phase.name+' напиши 1 чтобы продолжить\n' + str(phase.a) + ':' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.g +=1
            return True
        if phase.c != int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text(phase.surName+',неверно,напиши 1 чтобы продолжить\n' + str(phase.a) + ':' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.h += 1
            return True


def umnoChek(phase, update):
    if phase.check != 4:
        return False
    else:
        d = update.message.text
        logger.info("umnoCheck start")
        if phase.c == int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text(phase.surName+' молодец напиши 1 чтобы продолжить\n' + str(phase.a) + '*' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.g +=1
            return True
        if phase.c != int(d):
            phase.randMove = random.randrange(1, 5)
            update.message.reply_text('неверно '+phase.name+' напиши 1 чтобы продолжить\n' + str(phase.a) + '*' + str(phase.b) + '=' + str(phase.c)+'\n решено верно:'+str(phase.g)+'\n ошибок:'+ str(phase.h))
            phase.check = 0
            phase.h += 1
            return True


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




def getUserContext(update):
    key = update.message.chat.username
    userData = users.get(key)
    if userData is None:
        userData = Phase()
        users[key] = userData
    return userData


users = {}
masiv = [hi, surname, startMaths, plasCheck, plas,min,minCheck,umno,umnoChek,delen,delenChek]


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
