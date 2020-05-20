import logging
from datetime import datetime, timedelta
from threading import Timer
from dataclasses import dataclass

import telegram

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass()
class Data:
    user_to_ban = None
    userName_to_ban = None
    mess_from_user = None
    chat_id = None
    message_id = None
    message_to_delete = None
    chat_name = None
    phase = 0
    ban = []
    unban = []


data = Data()
bot = telegram.Bot('Токен')


def delete_message():
    data.message_to_delete += 1
    bot.delete_message(chat_id=data.chat_id, message_id=data.message_to_delete)


def ban_user(update, message):
    if data.phase == 0:
        data.phase = 1
        data.ban = []
        data.unban = []
        data.chat_name = update.message.chat.username
        data.user_to_ban = update.message.reply_to_message.from_user.id
        data.userName_to_ban = update.message.reply_to_message.from_user.first_name
        data.message_id = update.message.message_id
        data.chat_id = update.message.chat.id
        bot.delete_message(chat_id=data.chat_id, message_id=data.message_id)
        data.message_id += 1
        bun_button = [[InlineKeyboardButton(text='за бан', callback_data='за'),
                       InlineKeyboardButton(text='против бана', callback_data='против')]]
        bun_button = InlineKeyboardMarkup(bun_button)
        bun_text = 'Забанить {}?'.format(data.userName_to_ban)
        bot.send_message(chat_id=data.chat_id, text=bun_text, reply_markup=bun_button)
        timer = Timer(60 * 30, kik)
        timer.start()
    else:
        data.message_to_delete = update.message.message_id
        bot.delete_message(chat_id=data.chat_id, message_id=data.message_to_delete)
        url = 'https://t.me/{}/{}'.format(data.chat_name, data.message_id)
        button = [[InlineKeyboardButton(text='голосовать', url=url)]]
        button = InlineKeyboardMarkup(button)
        bot.send_message(chat_id=data.chat_id, text='Сейчас нельзя подавать на бан.\nНо вы можете проголосовать.', reply_markup=button)
        timer = Timer(60, delete_message)
        timer.start()


def golosa(update, context):
    query = update.callback_query
    query.answer()
    user = update._effective_user.id
    user_name = update._effective_user.first_name
    count = 0
    count1 = 0
    if user_name == data.userName_to_ban:
        pass
    else:
        if format(query.data) == 'за':
            if user in data.unban:
                data.unban.remove(user)
                data.ban.append(user)
            else:
                if user in data.ban:
                    data.ban.remove(user)
                else:
                    data.ban.append(user)
            count = data.ban.__len__()
            count1 = data.unban.__len__()
        if format(query.data) == 'против':
            if user in data.ban:
                data.ban.remove(user)
                data.unban.append(user)
            else:
                if user in data.unban:
                    data.unban.remove(user)
                else:
                    data.unban.append(user)
            count = data.ban.__len__()
            count1 = data.unban.__len__()
        bun_button = [[InlineKeyboardButton(text='за бан: ' + str(count), callback_data='за'),
                       InlineKeyboardButton(text='против бана: ' + str(count1), callback_data='против')]]
        bun_button = InlineKeyboardMarkup(bun_button)
        bun_text = 'Забанить {}?'.format(data.userName_to_ban)
        query.edit_message_text(reply_markup=bun_button, text=bun_text)


def kik():
    data.phase = 0
    count_user = data.ban.__len__() - data.unban.__len__()
    bot.delete_message(chat_id=data.chat_id, message_id=data.message_id)
    if count_user >= 2:
        bot.send_message(chat_id=data.chat_id, text='пользователь {} удалён'.format(data.userName_to_ban))
        bot.kick_chat_member(chat_id=data.chat_id, user_id=data.user_to_ban)
    else:
        bot.send_message(chat_id=data.chat_id, text='пользователь не удалён')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("Токен", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("ban_user", ban_user))
    updater.dispatcher.add_handler(CallbackQueryHandler(golosa))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
