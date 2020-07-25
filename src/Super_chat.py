import os
from time import sleep

from voven4ek_html import *
from flask import Flask, request, render_template, make_response, session
from threading import Timer

app = Flask(__name__, template_folder="/home/vova492/IdeaProjects/pythonTest/src")
secret_key(app)
img = 'https://img3.goodfon.ru/original/1920x1080/f/d6/makro-zelen-trava-listya.jpg'


def clear():
    while True:
        with open('chat.txt', 'w+'):
            pass
        f = open('chat.txt', 'a')
        f.write('Super_chat:::Чат очишен!')
        f.close()
        sleep(120)


t = Timer(0, clear)
t.start()


class User:
    username = None
    surname = None
    reg = 0


user = User()


@app.route('/')
def home_page():
    mas = [
        bg_color('yellow'),
        zagolovok('Добро пожаловать в ' + strong('Super_chat'), 'Super_chat'),
        body('green'),
        bg_color_close(),
        form('get_user_data'),
        page_text('Ваше имя', 3, color='blue'),
        input_data('text', 'username', '', 'Больше 3 символов'),
        page_text('Ваша фамилия', 3, color='blue'),
        input_data('text', 'surname', '', 'Больше 3 символов'),
        br(),
        br(),
        input_data('submit', 'submit', 'Принять', ''),
        input_data('reset', 'reset', 'Сбросить', ''),
        form_close()
    ]
    
    return colektor(mas)


@app.route('/get_user_data', methods=['post', 'get'])
def get_user_data():
    session['username'] = request.form.get('username')
    session['surname'] = request.form.get('surname')
    l = list(session['username'])
    l2 = list(session['surname'])
    if l.__len__() > 3 and l2.__len__() > 3:
        session['reg'] = 1
        mas = [
            bg_color('gray'),
            zagolovok(text_color('Всё в норме!', 'blue'), 'Super_chat'),
            body('green'),
            page_text(url('super_chat', 'Нажмие, чтобы войти в чат'), 2),
            bg_color_close(),
            br(),
        ]
        return colektor(mas)
    else:
        mas = [
            zagolovok(text_color('Имя или фамилия слишком короткие!', 'red'), 'Ошибка'),
            body('green'),
            button('Назад', '/')
        ]
        return colektor(mas)


@app.route('/super_chat')
def super_chat():
    try:
        if session['reg'] == 1:
            messages = []
            file = open('chat.txt', 'r')
            while True:
                text = file.readline()
                if not text:
                    break
                text = text.split(':::')
                user1 = text[0]
                mes = text[1]
                if mes != '' and mes != '\n':
                    text = '<strong>{} пишет:</strong><br><i><ul>{}</ul></i><br><br>'.format(user1, mes)
                    messages.append(text)
            file.close()
            mas = [
                zagolovok(text_color('Super_chat', 'gold'), 'Super_chat'),
                body('green'),
                lot_of_text(messages),
                form('send_message'),
                """
                <meta http-equiv="refresh" content="10">
                <div id="x">
                <input type='text' size='100' name='message' autofocus>
                <input type='submit' value='отправить'>
                </div>
                
                <style>
                    #x{
                        position:fixed;
                        bottom:0;
                        left:0
                    }
                </style>
                """,
                form_close()
            ]
            return colektor(mas)
    except KeyError:
        mas = [
            zagolovok('Для того чтобы пользоваться чатом зарегестрируйтесь!', 'registr'),
            body('green'),
            button('Зарегистрироваться!', '/')
        ]
        return colektor(mas)


@app.route('/send_message', methods=['post'])
def send_message():
    if session['reg'] == 1:
        message11 = request.form.get('message')
        f = open('chat.txt', 'a')
        message11 = session['username'] + ' ' + session['surname'] + ':::' + message11
        f.write('\n' + str(message11))
        f.close()
        return move_prev()


if __name__ == "__main__":
    app.run(host='192.168.8.102')
