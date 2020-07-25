import os
from time import sleep

from voven4ek_html import *
from flask import Flask, request, render_template, make_response, session
from threading import Timer

app = Flask(__name__, template_folder="/home/vova492/IdeaProjects/pythonTest/src")
app.config['SECRET_KEY'] = os.urandom(20).hex()


@app.route('/')
def home_page():
    mas = [
        zagolovok(text_color('Добро пожаловать на forum!', '#AC1B23'), 'forum'),
        br(),
        body('#998CC9'),
        page_text(red_string('Наши темы:'), 3),
        abzac(),
        abzac(),
        punkt(
            url('program', 'Програмирование')
        ),
        br(),
        punkt(
            url('tema2', 'tema')
        ),
        abzac_close(),
        abzac_close()
    ]
    return colektor(mas)


@app.route('/program')
def tema_program():
    mas = [
        zagolovok('Что вы выбирете?', 'програмирование'),
        br(),
        page_text('Наши темы по програмированию!', 3, 'brown'),
        abzac(),
        punkt(
            url('ques', 'Вопросы')
        ),
        abzac_close(),
    ]
    return colektor(mas)


if __name__ == "__main__":
    app.run(host='192.168.8.102')
