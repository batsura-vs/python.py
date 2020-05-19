import logging
from datetime import datetime, timedelta
from threading import Timer
from dataclasses import dataclass

import telegram

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CallbackQueryHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass()
class Data:
    message_id = None
    user = None
    chat_id = None
    user_id = None
    timer = None
    d_mes = None


data = Data()

bot = telegram.Bot('Токен')


def delete_mes():
    data.d_mes += 1
    bot.delete_message(chat_id=data.chat_id, message_id=data.d_mes)


def delete_user():
    mes_text = 'Очень жаль {},но вы не прошли проверку'.format(data.user)
    bot.send_message(chat_id=data.chat_id, text=mes_text)
    bot.kick_chat_member(chat_id=data.chat_id, user_id=data.user_id)
    t = Timer(15, delete_mes)
    t.start()
    delete_mes()


def new_member(update, context):
    data.timer = Timer(30, delete_user)
    data.message_id = update.message.message_id
    data.chat_id = update.message.chat.id
    data.user_id = update.message.from_user.id
    data.user = update.message.from_user.first_name
    data.d_mes = data.message_id
    test = [[InlineKeyboardButton(text='нажмите на кнопку!', callback_data='pressed')]]
    test = InlineKeyboardMarkup(test)
    mes_text = 'здравствуйте {},пройдите проверку(у вас есть 30сек)'.format(data.user)
    bot.restrict_chat_member(data.chat_id, data.user_id, permissions=telegram.ChatPermissions(can_send_messages=False,
                                                                                              can_send_other_messages=False))
    bot.send_message(chat_id=data.chat_id, text=mes_text, reply_markup=test, reply_to_message_id=data.message_id)
    data.timer.start()


def button_is_pressed(update, context):
    query = update.callback_query
    query.answer()
    user_press = update._effective_user.id
    if user_press != data.user_id:
        pass
    elif format(query.data) == 'pressed':
        data.timer.cancel()
        bot.restrict_chat_member(data.chat_id, data.user_id,
                                 permissions=telegram.ChatPermissions(can_send_messages=True,
                                                                      can_send_other_messages=True))
        rules = [[InlineKeyboardButton(text='Правила чата.', url='Твоя ссылка на правила')]]
        rules = InlineKeyboardMarkup(rules)
        query.edit_message_text('Проверка пройдена', reply_markup=rules)
        t = Timer(15, delete_mes)
        t.start()

def delete_left_mes(update,context):
    mes_to_delete = update.message.message_id
    chat = update.message.chat.id
    bot.delete_message(chat, mes_to_delete)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("Токен", use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, delete_left_mes))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_is_pressed))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
