import logging
from random import random
from time import sleep
from dataclasses import dataclass

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, TelegramError, \
    ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
from array import array

@dataclass
class Phase:
    step = 0
    d = 0
    s = 0
    v = 0
    x = 0
    c = 0
    z = 0
    first: str
    second: str
    fird: str
    fourd: str
    fifs: str
    six: str
    q = 0
    key: str
    key1: str
    asw = 0
    pupl :str
    name = str
    id = None

puples = []


def start(update, context, ):
    phase.id = update.message.from_user.id
    phase.pupl = update.message.from_user.first_name
    if str(phase.pupl) in puples:
        pass
    else :
        st = [[InlineKeyboardButton("пройти проверку", callback_data='start')]]
        star = InlineKeyboardMarkup(st)
        update.message.reply_text("здравствуйте "+phase.pupl+" пройдите проверку",reply_markup=star)



def button1(update, context):
    print(phase.id)
    print(phase.pupl)
    query = update.callback_query
    query.answer()
    print(update.callback_query.id)
    if format(query.data) == 'start':
        from random import randrange
        kods = [[InlineKeyboardButton("запомнил(а)", callback_data='kodGet')]]
        f = InlineKeyboardMarkup(kods)
        while phase.q == 0:
            phase.d = randrange(10, 100)
            phase.z = randrange(10, 100)
            phase.c = randrange(10, 100)
            phase.s = randrange(10, 100)
            phase.v = randrange(10, 100)
            phase.x = randrange(10, 100)
            if phase.z != phase.d and phase.d != phase.c and phase.d != phase.s and phase.d != phase.v and phase.d != phase.x and phase.z != phase.c and phase.z != phase.s and phase.z != phase.v and phase.z != phase.x and phase.c != phase.s and phase.c != phase.v and phase.c != phase.x and phase.v != phase.x:
                phase.q = 1
        sd = randrange(1, 7)
        if sd == 1:
            phase.first = 'yes'
            phase.second = 'no'
            phase.fird = 'no'
            phase.fourd = 'no'
            phase.fifs = 'no'
            phase.six = 'no'
            query.edit_message_text(text=" запомните это число:" + str(phase.x), reply_markup=f)
        if sd == 2:
            phase.first = 'no'
            phase.second = 'yes'
            phase.fird = 'no'
            phase.fourd = 'no'
            phase.fifs = 'no'
            phase.six = 'no'
            query.edit_message_text(text=" запомните это число:" + str(phase.v), reply_markup=f)
        if sd == 3:
            phase.first = 'no'
            phase.second = 'no'
            phase.fird = 'yes'
            phase.fourd = 'no'
            phase.fifs = 'no'
            phase.six = 'no'
            query.edit_message_text(text=" запомните это число:" + str(phase.d), reply_markup=f)
        if sd == 4:
            phase.first = 'no'
            phase.second = 'no'
            phase.fird = 'no'
            phase.fourd = 'yes'
            phase.fifs = 'no'
            phase.six = 'no'
            query.edit_message_text(text=" запомните это число:" + str(phase.c), reply_markup=f)
        if sd == 5:
            phase.first = 'no'
            phase.second = 'no'
            phase.fird = 'no'
            phase.fourd = 'no'
            phase.fifs = 'yes'
            phase.six = 'no'
            query.edit_message_text(text=" запомните это число:" + str(phase.z), reply_markup=f)
        if sd == 6:
            phase.first = 'no'
            phase.second = 'no'
            phase.fird = 'no'
            phase.fourd = 'no'
            phase.fifs = 'no'
            phase.six = 'yes'
            query.edit_message_text(text=" запомните это число:" + str(phase.s), reply_markup=f)
    if format(query.data) == 'kodGet':
        kodi = [[InlineKeyboardButton(str(phase.x), callback_data=phase.first)],
                [InlineKeyboardButton(str(phase.v), callback_data=phase.second)],
                [InlineKeyboardButton(str(phase.d), callback_data=phase.fird)],
                [InlineKeyboardButton(str(phase.c), callback_data=phase.fourd)],
                [InlineKeyboardButton(str(phase.z), callback_data=phase.fifs)],
                [InlineKeyboardButton(str(phase.s), callback_data=phase.six)]]
        a = InlineKeyboardMarkup(kodi)

        name = update.callback_query["from"].username
        print(name)
        bot.answer_callback_query(text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉',callback_query_id=phase.name, show_alert=True)
        if phase.id == phase.name:
            query.edit_message_text('где ваше число', reply_markup=a)
    if format(query.data) == 'yes':
        kodp = [[InlineKeyboardButton("да", callback_data='yes1'),
                 InlineKeyboardButton("нет", callback_data='no1')]]
        kodprom = InlineKeyboardMarkup(kodp)
        query.edit_message_text(phase.pupl+' вы человек?', reply_markup=kodprom)
    if format(query.data) == 'no':
        query.edit_message_text('очень жаль ' + phase.pupl + ' ,но вы не прошли проверку,\nпохоже вы робот')
        bot.kickChatMember(chat_id = -1001314131082,user_id = phase.name)
    if format(query.data) == 'no1':
        query.edit_message_text('ну тест прошли вы как человек')
        phase.step = 1
        puples.append(phase.pupl)
        print(puples)
        if format(query.data) == 'yes1':
            phase.step = 1
            query.edit_message_text('проверка пройдена успешно,добро пожаловать '+phase.pupl)
            puples.append(phase.pupl)
            print(puples)

bot = telegram.Bot("1037824337:AAGxeQ7N8iPNeGx1BZBZHhMEm_8jKrfbkRQ")

def button(update, context):
        query = update.callback_query
        query.answer()
        sleep(10)

        query.edit_message_text(text="это бот для теста кнопок")


def help(update, context):
    if phase.step == 1:
        keyboard = [[InlineKeyboardButton("наша группа", url='https://t.me/BrawlStarsStore492')],
                    [InlineKeyboardButton("инструкции", callback_data='infa'),
                     InlineKeyboardButton("дальше", callback_data='next')],
                    [InlineKeyboardButton("о нас", callback_data='text')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('перейдите по кнопке:', reply_markup=reply_markup)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


users = {}

def getUserContext(update):
    key = update.message.chat.username
    userData = users.get(key)
    if userData is None:
        update.message.reply_text('Здравствуйте зарегестрируйтесь пожалуйста /start')
        userData = phase()
        users[key] = userData
    return userData


masiv = []
phase=Phase

def sborka(update, context):
    phase = getUserContext(update)
    for handler in masiv:
        if handler(phase, update) is True:
            return

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1037824337:AAGxeQ7N8iPNeGx1BZBZHhMEm_8jKrfbkRQ", use_context=True)
    dp = updater.dispatcher
    updater.dispatcher.add_handler(MessageHandler(Filters.text, start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button1))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
