from dataclasses import dataclass
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


def hi(phase, update):
    logger.info('hi', phase.phase)
    if phase.phase == 0:
        update.message.reply_text('привет, как тебя зовут?')
        phase.phase += 1
        return True
    else:
        return False


def surname(phase, update):
    logger.info('surname', phase.phase)
    if phase.phase == 1:
        update.message.reply_text('а какая фамилия у тебя?')
        phase.phase += 1
        return True
    else:
        return False


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def born(phase, update):
    logger.info('born', phase.phase)
    if phase.phase == 2:
        try:
            update.message.reply_text('твой год рождения в формате дд.мм.гггг')
            god = update.message.text
            rod = datetime.strptime(update.message.text, '%d.%m.%Y')
            phase.phase += 1
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
