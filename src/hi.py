import logging
from random import random
from threading import Timer
from time import sleep
from dataclasses import dataclass

import telegram

from telegram import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, TelegramError, \
    ReplyKeyboardRemove, Update, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, dispatcher, \
    CallbackContext

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
    query_id = None
    fifs: str
    six: str
    user = None
    q = 0
    key: str
    bun1 = None
    key1: str
    asw = 0
    kikU = 0
    Unkik = 0
    pupl: None

    name = str
    id = None
    mId = 0
    t = None
    chat = None
    chat1 = None
    pupl = None


bun = []
mat = ['test', 'hi']


def prog(update, context):
    phase.pupl = update.message.from_user.first_name
    phase.id = update.message.from_user.id
    phase.chat = update.message.chat.id
    phase.mess = 1
    phase.bun1 = phase.id
    st = [[InlineKeyboardButton("пройти проверку", callback_data='start')]]
    star = InlineKeyboardMarkup(st)
    update.message.reply_text("здравствуйте " + phase.pupl + " пройдите проверку (у вас есть минyта)",
                              reply_markup=star)
    phase.t = Timer(60.0, delit)
    phase.t.start()
    phase.name = update._effective_user.first_name


bot = telegram.Bot("1037824337:AAGxeQ7N8iPNeGx1BZBZHhMEm_8jKrfbkRQ")


def delit():
    bot.kickChatMember(chat_id=phase.chat, user_id=phase.id)


golosa = []


def button1(update, context):
    print(phase.id)
    print(phase.pupl)
    query = update.callback_query
    query.answer()
    print(update.callback_query.id)
    if format(query.data) == 'start':
        phase.name = update._effective_user.first_name
        if phase.pupl == phase.name:
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
            print(phase.name, phase.pupl)
            if phase.pupl == phase.name:
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
                phase.name = update._effective_user.first_name
    if format(query.data) == 'kodGet':
        kodi = [[InlineKeyboardButton(str(phase.x), callback_data=phase.first)],
                [InlineKeyboardButton(str(phase.v), callback_data=phase.second)],
                [InlineKeyboardButton(str(phase.d), callback_data=phase.fird)],
                [InlineKeyboardButton(str(phase.c), callback_data=phase.fourd)],
                [InlineKeyboardButton(str(phase.z), callback_data=phase.fifs)],
                [InlineKeyboardButton(str(phase.s), callback_data=phase.six)]]
        print(phase.name, phase.pupl)
        a = InlineKeyboardMarkup(kodi)
        phase.name = update._effective_user.first_name
        if phase.pupl == phase.name:
            query.edit_message_text('где ваше число', reply_markup=a)
            phase.name = update._effective_user.first_name
    if format(query.data) == 'yes':
        print(phase.name, phase.pupl)
        phase.name = update._effective_user.first_name
        if phase.pupl == phase.name:
            phase.t.cancel()
            phase.step = 1
            file = open("stop.txt", "a")
            file.write(',' + phase.pupl)
            file.close()
            query.edit_message_text('проверка пройдена успешно,добро пожаловать ' + phase.pupl)
            phase.mess = 0
            print(phase.mess)
    if format(query.data) == 'no':
        print(phase.name, phase.pupl)
        phase.name = update._effective_user.first_name
        if phase.pupl == phase.name:
            phase.t.cancel()
            query.edit_message_text('очень жаль ' + phase.pupl + ' ,но вы не прошли проверку,\nпохоже вы робот')
            bot.kickChatMember(chat_id=phase.chat, user_id=phase.id)
            phase.mess = 0
            print(phase.mess)
    print('hahahaha')
    if format(query.data) == 'za':
        us = update._effective_user.first_name
        if us in golosa:
            pass
        else:
            id = update.callback_query.id
            bot.answer_callback_query(callback_query_id=id, text='вы уже голосовали', show_alert=True)
            golosa.append(us)
            phase.kikU += 1
    if format(query.data) == 'protiv':
        phase.Unkik += 1
    if phase.kikU - phase.Unkik >= 2:
        bot.kick_chat_member(chat_id=phase.chat, user_id=phase.user)
        query.edit_message_text(text='пользователя удалили')
        phase.Unkik = 0
        phase.kikU = 0


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


users = {}


def getUserContext(update):
    key = update.message.chat.username
    userData = users.get(key)
    if userData is None:
        userData = phase()
        users[key] = userData
    return userData


masiv = []
phase = Phase


def sborka(update, context):
    phase = getUserContext(update)
    for handler in masiv:
        if handler(phase, update) is True:
            return


kik = []


def left(update, context):
    mesId = update.message.id
    chat = update.message.chat.id
    bot.delete_message(chat_id=chat, message_id=mesId)


golos = [[InlineKeyboardButton('за удаление', callback_data='za')],
         [InlineKeyboardButton('против', callback_data='protiv')]]
golos = InlineKeyboardMarkup(golos)


def bad_user(update, context):
    phase.chat = update.message.chat.id
    phase.user = update.message.reply_to_message.from_user.id
    phase.query_id = phase.user + 1
    name = update.message.reply_to_message.from_user.first_name
    bot.send_message(chat_id=phase.chat, text='удалить пользователя' + name, reply_markup=golos)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1037824337:AAGxeQ7N8iPNeGx1BZBZHhMEm_8jKrfbkRQ", use_context=True)
    dp = updater.dispatcher
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, prog))
    updater.dispatcher.add_handler(CallbackQueryHandler(button1))
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, left))
    dp.add_handler(CommandHandler("bad_user", bad_user))

    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
