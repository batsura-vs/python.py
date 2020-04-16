from dataclasses import dataclass
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

@dataclass
class Phase():
    phase2=1
    d=0
    s=None
    a=None

handlers = []

def number(update,phase2):
    if phase2==1:
        update.message.reply_text('введите сколько букв вы хотите поменять')
        phase2+=1
        return True

def numberCheck(update,phase2):
    if phase2==2:
        Phase.d=update.message.text
        phase2+=1
        return True


def slovo(update,phase2):
    if phase2==3:
        update.message.reply_text('введи 1 слово')
        phase2+=1
        return True

def slovoCheck(update,phase2):
    if phase2==4:
        Phase.s=update.message.text
        phase2+=1
        return True

def slovo2(phase2,update):
    if phase2 == 5:
        update.message.reply_text('введи 2 слово')
        phase2+=1
        return True

def slovo2Check(update,phase2):
    if phase2== 6:
        Phase.a=update.message.text
        phase2+=1
        return True

def sborka(update,phase2):
    if phase2==7:
        asf = Phase.s[Phase.d]
        sf = Phase.s[Phase.d:]
        b = len(Phase.s)
        n = len(sf)
        x = b - n
        z = Phase.s[:x]

        zx = Phase.a[Phase.d]
        xz = Phase.a[Phase.d:]
        vb = len(Phase.a)
        zn = len(sf)
        vx = b - n
        mn = Phase.a[:vx]
        update.message.reply_text(z + xz, mn + sf,'    напиши что-нибудь')
        phase2=1
        return True

handler = [sborka,number,slovo,slovoCheck,slovo2,slovo2Check]

def handleEvent(update, context):
    """Echo the user message."""

    logger.info(update.message.chat.username)
    logger.info(Phase.phase2)

    for handler in handlers:
        if handler(Phase.phase2, update) is True:
            return


"""userData = PassportData()

i = 0
while handeEvent(userData):
    i += 1

printData(userData)
"""


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("995509965:AAFapX8o5vYD7erMtAmS5ExxI-G0hKcApJE", use_context=True)
    dp = updater.dispatcher
    echo_handler = MessageHandler(Filters.text, handleEvent)
    dp.add_handler(echo_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
