from tkinter import *
from dataclasses import dataclass
from tkinter import messagebox


@dataclass
class phase():
    saveTxt = None
    f = None
    m = None
    dfd = None


def e ():
    print(phase.f)
    fales.write(str(phase.m)+'.'+phase.dfd.get()+'\n\n')
    file()


def con():
    phase.asd = open('/home/vova492/z.txt','r+')
    phase.m = phase.asd.read()
    phase.m = phase.m.__len__()
    if phase.m ==0:
        phase.m+=1
        phase.asd.write('1')
    phase.asd.write('1')
    e()


def delate():
    with open('/home/vova492/r.txt', 'wb'):
        pass
    with open('/home/vova492/z.txt', 'wb'):
        pass


def re():
    fales = open('/home/vova492/r.txt','r+')
    d = fales.read()
    messagebox.showinfo('заметка',d)


def file():
    phase.dfd = Entry(window, width=90,font=("Courier New", 13))
    phase.dfd.grid(column=5, row=5)
    phase.dfd.focus()
    phase.f = phase.dfd.get()
    print(phase.dfd)
    print(phase.f)
    btn = Button(window, text="сохранить",font=("Arial Bold", 15), command=con)
    btn.grid(column=6, row=6)
    btn = Button(window, text="удалить всё",font=("Arial Bold", 15), command=delate)
    btn.grid(column=6, row=7)
    btn = Button(window, text="все заметки",font=("Arial Bold", 15), command=re)
    btn.grid(column=6, row=8)



window = Tk()
fales = open('/home/vova492/r.txt','r+')
btn = Button(window,text = 'заметки',font=("Arial Bold", 15),command = file)
btn.grid(column=6, row=1)
d = fales.read()
messagebox.showinfo('заметки',d)
window.mainloop()
