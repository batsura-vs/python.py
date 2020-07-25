import os
import sqlite3
from functools import wraps
from random import randrange

from flask import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header

app = Flask(__name__, template_folder="/home/vova492/IdeaProjects/pythonTest/src")
app.config['SECRET_KEY'] = os.urandom(20).hex()
table = 'voven4ek.db'


def do_hash(text):
    characters = list('''1234567890_!@#$%^&*()+-
    qwertyuiop[]\;';lkjhgfdsa\'/.,mnbvcxz
    йцукенгшщзхъё
    фывапролджэячсмитьбю
    QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗФЫВАПРОЛДЖЭЯЧСМИТЬБЮ?''')

    text = list(text)
    hah = text.__len__()
    l = text.__len__()
    for t in text:
        hah = int(int(hah) + int(t.__len__() * 2 * l) + int(characters.index(t) * l)) * characters.__len__() / 15356798
    return hah


def add(entities):
    con = sqlite3.connect(table)
    sup = con.cursor()
    sup.execute(
        'INSERT INTO user_data(username, gmail, password)'
        ' VALUES(?, ?, ?)',
        entities)

    con.commit()
    con.close()


def is_login(func):
    @wraps(func)
    def login(*args, **kwargs):
        if 'login' in session:
            return func(*args, **kwargs)
        else:
            html = """
            <html>
            <head>
            <h2>Извините, но вы не зарегистрированны!</h2>
            </head>
            <style>
               body {
                background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
                -moz-background-size: 100%; /* Firefox 3.6+ */
                -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
                -o-background-size: 100%; /* Opera 9.6+ */
                background-size: 100%; /* Современные браузеры */
               }
              </style>
            <body>
            Что-бы получить доступ к этой странице!
            <br>
            Перейдите по <a href="/">этой</a> ссылке!
            </body>
            </html>
            """
            return html

    return login


def read(element, what, than):
    con = sqlite3.connect(table)
    sup = con.cursor()
    sup.execute('SELECT ' + element + ' FROM user_data where ' + what + than)

    rows = sup.fetchall()
    mas = []
    for row in rows:
        mas.append(row[0])
    con.close()
    return mas


def edit_tab(edit, ready, what, that):
    con = sqlite3.connect(table)
    sup = con.cursor()
    sup.execute('UPDATE user_data SET ' + edit + ' = ' + ready + ' where ' + what + ' = ' + that + '')

    con.commit()
    con.close()


def send_gmail(text, zagolovok, to):
    # Настройки
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    # Формируем тело письма

    subject = zagolovok
    body = text
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # Отправляем письмо
    server.login('voven4ek@gmail.com', 'vova1vova')
    server.sendmail('voven4ek@gmail.com', to, msg.as_string())
    server.quit()  # Выходим


@app.route('/')
def reg():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>registr</title>
        <div id="hi">
            <h1>Здравствуйте, пройдите регистрацию пожалуйста!</h1>
        </div>
    </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
    <body>
        <div id="x">
            Уже есть аккаунт?
        <a href="/vhod">Войти</a>
        </div>
        <style type="text/css">
                        #x {
                                position: relative;
                                left: 1000px;
                                top: 15px;
                               }
        </style>
        <form action="reg" method="post">
            <div id="regist">
                Ваше имя
                <br>
                <input type="text" placeholder="Ваше имя" name="name">
                <br>            <br>
    
                Ваш Gmail
                <br>
                <input type="text" placeholder="Ваш Gmail" name="gmail">
                <br>            <br>
    
                Придумайте пароль
                <br>
                <input type="password" placeholder="Придумайте пароль" name="pas1">
                <br>            <br>
    
                Повторите пароль
                <br>
                <input type="password" placeholder="Повторите пароль" name="pas2">
                <br>
                <input type="submit" value="Зарегистрироваться">
                <input type="reset" value="Сбросить">
            </div>
        </form>
        <style>
            #regist{
            position: relative;
            top:100px;
            left:15px
            }
        </style>
    </body>
    </html>
    """
    return html


@app.route('/reg', methods=['POST'])
def reg12():
    session['username'] = request.form.get('name')
    session['gmail'] = request.form.get('gmail')
    session['pas1'] = request.form.get('pas1')
    con = sqlite3.connect(table)
    sup = con.cursor()
    sup.execute('SELECT gmail FROM user_data')
    rows = sup.fetchall()
    mas = []
    for row in rows:
        mas.append(row[0])
    con.close()
    if list(session['username']).__len__() < 2 or list(session['pas1']).__len__() < 8:
        return 'Слишком короткое имя или пароль повторите <a href="/">попытку!</a>'
    elif session['gmail'] not in mas:
        try:
            session['pas1'] = do_hash(request.form.get('pas1'))
            session['pas2'] = do_hash(request.form.get('pas2'))
            session['kod'] = randrange(100000, 999999)
            if str(session['pas1']) == str(session['pas2']):
                send_gmail('Здравствуйте {}!\nКод для подтверждения: {}. \nНи кому не сооб'
                           'щайте код!'.format(session['username'],
                                               session['kod'])
                           , 'Код подтверждения с сайта voven4ek', session['gmail'])
                html = '''
                <html>
                <head>
                <h1>Введите код из письма</h1>
                </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>''' + '''
                <body>
                <form action="/kod" method="post">
                <h3>Введите код из писма отправленого на электроную почту: "{}"</h3>
                <input type="text" name="kod">
                <input type='submit' value='отправить'>
                </form>
                </body>
                </html>'''.format(session['gmail'])
                return html
            else:
                return 'Пароли не совпадают! Вернуться <a href="/">назад?</a>'
        except:
            return 'Не верная почта!!! Вернуться <a href="/">назад?</a>'
    else:
        return """
        <html>
        <head>
        <h1>Почта: "{}" уже зарегистрирована.</h1>""".format(session['gmail']) + """
        </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
        <body>
        <div id='url'>
        <h1>Используйте ссылку, что-бы <a href="/vhod">Войти</a></h1>
        </div>
        <style>
            #url{
            position: relative;
            left: 280;
            top: 125
            }
        </style>
        </body>
        </html>
        """


@app.route('/kod', methods=['POST'])
def kod12():
    kod1 = request.form.get('kod')
    if kod1 == str(session['kod']):
        session['login'] = 'login'
        add([session['username'], session['gmail'], session['pas1']])
        return '''
        <html>
        <head>
        <h1>Код верный!</h1>
        </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
        <body>
        Перейти к <a href="/home_page">сайту!</a>
        </body>
        </html>
        '''
    else:
        return '''
        <html>
        <head>
            <h1>Код не верный! Повторите <a href="/">попытку!</a></h1>
        </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
        <body>
        </body>
        </html>
        '''


@app.route('/vhod')
def vhod():
    return """
    <html>
    <head>
    <h1>Войти в систему могут только зарегистрированные пользователи!</h1>
    <title>Вход</title>
    </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
    <body>
    <form action='vhod_key' method='POST'>
    <div id='reg'>
    <h3>Ваша элэктронная почта</h3>
    <input type='text' placeholder="Элэктронная почта" name="gmail">
    <br>
    <input type='submit' value='Отправить'>
    </div>
    <div id='email'>
    <h3>Ваш пароль</h3>
    <input type='password' placeholder="Пароль" name="password">
    <br>
    <input type='reset' value='Сбросить'>
    </div>
    </form>
    <a href='/swap'><button>Сбросить пароль</button></a>
    <style>
        #reg{
            position: relative;
            left: 0;
            top: 19
            }
    </style>
    <style>
        #email{
            position: relative;
            left: 285;
            bottom: 100
            }
    </style>
    <div id='text'>
    Войти в систему могут только зарегистрированные пользователи!
    <br>
    Если вы всё ещё не зарегистрированны вы можете зарегистрироваться по <a href='/'>ссылке.</a>
    </div>
    <style>
        #text{
            position: relative;
            left: 0;
            bottom: 90
    </style>
    </body>
    </html>
    """


@app.route('/vhod_key', methods=["POST"])
def vhod_key():
    try:
        gmail = request.form.get('gmail')
        session['gmail'] = gmail
        password = str(do_hash(request.form.get('password')))
        pas = read('password', 'gmail=', '\'' + gmail + '\'')[0]
        session['username'] = read('username', 'gmail=\'', gmail + '\'')
        if password == pas and gmail == read('gmail', 'password=\'', str(password) + '\'')[0]:
            session['login'] = 'login'
            session['username'] = read('username', 'gmail=\'', gmail + '\'')[0]
            return '''
            <html>
            <head>
            <h1>Здравствуйте, {} добро пожаловать!</h1>
            </head>
            '''.format(session['username']) + '''<style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
            <body>
            <div id='text'>
            <h1>Перейти к <a href="/home_page">сайту!</a></h1>
            </div>
            <style>
                #text{
                    position: relative;
                    left: 440;
                    top: 190
                    }
            </style>
            </body>
            </html>
            '''
        else:
            return """
            <html>
            <head>
            <h1>Не верный логин или пароль!</h1>
            </head>
            <body>
            <h3><a href='/vhod'>Повторите попытку</a>
             или если вы не зарегистрированны можете <a href='/'>зделать это!</a></h3>
            </body>
            </html>
            """
    except IndexError:
        return '''
        <html>
        <head>
        <h1>Эта почта не зарегистрирована! <a href='/vhod'>Повторите!</a></h1>
        </head>
        </html>
        '''


@app.route('/home_page')
@is_login
def home_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>voven4ek</title>
    <div id='el'>
    <big>Вы вошли как {}!</big>""".format(session['username']) + """
    <br>
    <a href='/profile'>
    <img src="https://img2.freepng.ru/20180331/wte/kisspng-computer-icons-user-clip-art-user-5abf13c11e13b5.8484957815224718731232.jpg"
    width="30" height="30" alt="lorem">
    </a> 
    </div>
    <style>
        #el{
        position: fixed;
        color: white;
        background-image:
         url(https://krot.info/uploads/posts/2020-01/1580409129_59-p-foni-dlya-saitov-s-gradientom-117.jpg);
        padding: 15px;
        right: 0;
        top: 0
        }
    </style>
    </head>
    <body background="https://i.pinimg.com/originals/6e/23/6c/6e236c1adf4498bdd5efd0795c5649b0.jpg">
    <!-- встроенные файлы будут введены автоматически -->
    
    </body>
    </html>
    """


@app.route('/profile')
@is_login
def profile():
    return """
    <html>
    <head>
    <h1><font color='white'>Это ваш профиль! Здесь вы можете!</font></h1>
    <title>profile</title>
    </head>
    <body background="https://i.pinimg.com/originals/6e/23/6c/6e236c1adf4498bdd5efd0795c5649b0.jpg">
    <div id='app'>
    <a href='/new_password'>
    <button>
    <img src="https://bumper-stickers.ru/27091-thickbox_default/kluch.jpg"
    wight='30' height='30'> 
    <big>Поменять пароль</big>
    </button>
    </a>
    <br>
    <br>
    <a href='/home_page'>
    <img src="https://nsportal.ru/sites/default/files/media/2019/01/10/7f62f74d1996a3e2e7ec69114d4e4d4b4c38ece4.png"
    wight='190' height='60'>
    </a>
    </div>
    <style>
    #app{
    position: relative;
    color: white;
    right: 0;
    top: 50
    }
    </body>
    </html>    
    """


@app.route('/swap')
def swap():
    return '''
        <html>
        <head>
        <h1>Введите данные!</h1>
        </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
        <body>
        <form action='/new_password' method='POST'>
        Ваша почта
        <br>
        <input type='text' name='gmail'>
        <br>
        <input type='submit' value='Подвердить'>
        </form>
        </body>
        </html>
        '''


@app.route('/new_password', methods=['POST'])
def new_pas():
    con = sqlite3.connect(table)
    sup = con.cursor()
    sup.execute('SELECT gmail FROM user_data')
    rows = sup.fetchall()
    mas = []
    for row in rows:
        mas.append(row[0])
    con.close()
    if 'gmail' not in session:
        session['gmail'] = request.form.get('gmail')
    if session['gmail'] in mas:
        session['kod'] = randrange(100000, 999999)
        send_gmail('Здравствуйте!\nКод для подтверждения: {}. \nНи кому не сооб'
                   'щайте код!'.format(session['kod'])
                   , 'Код подтверждения с сайта voven4ek', session['gmail'])
        return '''
            <html>
            <head>
            <h1>Введите данные!</h1>
            </head><style>
   body {
    background: url(https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg) no-repeat;
    -moz-background-size: 100%; /* Firefox 3.6+ */
    -webkit-background-size: 100%; /* Safari 3.1+ и Chrome 4.0+ */
    -o-background-size: 100%; /* Opera 9.6+ */
    background-size: 100%; /* Современные браузеры */
   }
  </style>
            <body>
            <form action='/kod_pas' method='POST'>
            Новый пароль
            <br>
            <input type='password' name='pas1'>
            <br>
            Код из письма
            <br>
            <input type='text' name='kod'>
            <br>
            <input type='submit' value='Подвердить'>
            </form>
            </body>
            </html>
            '''
    else:
        return '<h1>Почта не <a href="/">зарегестрирована!</a></h1>'


@app.route('/kod_pas', methods=['POST'])
def kod_pas():
    password = request.form.get('pas1')
    pas_len = list(password).__len__()
    mes_kod = request.form.get('kod')
    if pas_len < 8 and mes_kod == str(session['kod']):
        return '''
        <html>
        <head>
        <h1>Пароль не может быть меньше 8 символов!</h1>
        </head>
        <body background="https://funart.pro/uploads/posts/2020-04/1586532415_13-p-svetlo-biryuzovie-foni-25.jpg">
        <form action='/kod_pas' method='POST'>
        Новый пароль
        <br>
        <input type='password' name='pas1'>
        <br>
        Код тотже
        <br>
        <input type='text' name='kod'>
        <br>
        <input type='submit' value='Подвердить'>
        </form>
        </body>
        </html>
        '''
    elif mes_kod == str(session['kod']) and pas_len > 7:
        try:
            password = do_hash(password)
            edit_tab('password', '\'' + str(password) + '\'', 'gmail', '\'' + session['gmail'] + '\'')
            return 'Пароль изменён! Пойдем на <a href="/home_page">сайт?</a>'
        except:
            return '''
            <html>
            <head>
            <h1><font color='whiteВы не зарегистрированы! Зарегистрируемся на <a href="/">сайте?</a></font></h1>
            </head>
            <body background="https://i.pinimg.com/originals/6e/23/6c/6e236c1adf4498bdd5efd0795c5649b0.jpg">
            </body>
            </html>
        '''
    else:
        return '''
        <html>
        <head>
        <h1><font color='white'>Код не верный</font></h1>
        </head>
        <body  background="https://i.pinimg.com/originals/6e/23/6c/6e236c1adf4498bdd5efd0795c5649b0.jpg">
        </body>
        </html>
        '''


if __name__ == '__main__':
    app.run(host='192.168.1.131')
