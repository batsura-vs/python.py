from random import randrange
from tkinter import *
from dataclasses import dataclass
from tkinter import messagebox


@dataclass
class per():
    x = 0
    y = None
    z = 0


def tp():
    per.y = randrange(1, 5)
    per.x = randrange(1, 5)


def g():
    per.z = 1
    game()


def q():
    per.z = 1
    game()


def w():
    per.z = 1
    game()

def h():
    messagebox.showinfo('заметка','это текст задания')


def e():
    per.z = 1
    game()

def game():
    global osm
    if per.z == 0:
        start.configure(
            text='|================================|\n|ты проснулся на корабле.Кругом  |\n|никого.Что будешь делать?       |\n|================================|\n|        <|                      |\n|         |                      |\n|       __|----|                 |\n|      |0 0 0[] }                |\n|  |-------------------/         |\n|  |  skorostnoi      /          |\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n|================================|\n',font=("Arial Bold", 10),command = h)
        osm = Button(window, text='осмотреть корабль',font=("Arial Bold", 10), command=g)
        osm.grid(column=0, row=0)
    if per.z == 1:
        start.configure(text='на корабле есть три каюты,кухня и грузовой отсек.Куда пойдешь?',font=("Arial Bold", 10))
        kaut = Button(window, text='посмотреть каюты',font=("Arial Bold", 10), command=q)
        kaut.grid(column=0, row=2)
        kit = Button(window, text='  на кухню!!!   ',font=("Arial Bold", 10), command=w)
        kit.grid(column=0, row=3)
        gr = Button(window, text=' грузовой отсек ',font=("Arial Bold", 10), command=e)
        gr.grid(column=0, row=4)
        osm.destroy()


window = Tk()
fales = open('/home/vova492/pys.txt','r+')
messagebox.showinfo('наши победители',fales.read())
window.title("voven4ek's game")
window.geometry('1378x768')
start = Button(window, text='========\n[ИГРАТЬ]\n========',font=("Arial Bold", 10), command=game)
start.grid(column=1, row=0)
window.mainloop()
