from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#
class Phase(Enum):
    INPUT_FIRSTNAME = auto()
    INPUT_SURNAME = auto()
    INPUT_BORN = auto()
    DONE = auto()


@dataclass()
class PassportData:
    firstName: str
    surName: str
    born: datetime
    userId: str = "unknown"
    phase: Phase = Phase.INPUT_FIRSTNAME

    def __init__(self):
        self.userId = self.userId


def inputFirstName(data, update):
    if data.phase is not Phase.INPUT_FIRSTNAME:
        return False
    data.firstName = update.message.text
    update.message.reply_text('введи свою фамилию')
    data.phase = Phase(data.phase.value + 1)
    return True

def inputSurName(data, update):
    if data.phase is not Phase.INPUT_SURNAME:
        return False
    data.surName = update.message.text
    update.message.reply_text('Введите дату рождения в формате дд.мм.гггг')
    data.phase = Phase(data.phase.value + 1)
    return True

def printData(data, update):
    if data.phase is not Phase.DONE:
        return False
    update.message.reply_text('Ты {data.firstName}')
    return True

def inputBorn(data, update):
    if data.phase is not Phase.INPUT_BORN:
        return False
    try:
        data.born = datetime.strptime(update.message.text, '%d.%m.%Y')
        data.phase = Phase(data.phase.value + 1)
    except ValueError:
        update.message.reply_text('Введите дату рождения в формате дд.мм.гггг')
        return False
    return True


def getUserContext(update):
    key=update.message.chat.username
    userData=users.get(key)
    if userData is None:
        userData = PassportData()
    return userData

users={}

handlers = [inputFirstName, inputSurName, inputBorn, printData]

def handleEvent(update, context):
    """Echo the user message."""
    data = getUserContext(update)

    logger.info(update.message.chat.username)
    logger.info(data)

    for handler in handlers:
        if handler(data, update) is True:
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
    updater = Updater("1106434818:AAH1RTWxMFDTyj9EQ3LaIUN64s-7jkeQFPU", use_context=True)
    dp = updater.dispatcher
    echo_handler = MessageHandler(Filters.text, handleEvent)
    dp.add_handler(echo_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
