from dataclasses import dataclass


@dataclass
class sups:
    d: str
    c: str


supchik = ['борщ', 'куриный бульон','макарошки', 'пюрешка']


def sup():
    d = input('какой суп вам приготовить?\n           меню          \n1.борщ \n2.куриный бульон \n3.макарошки \n4.пюрешка \nчто закажете?\n')
    f = supchik.index(d)
    if f==1:
        print('f')
        #описать борщь какой он на вкус ,запах,как ты его ешь
        return True
    if f==2:
        print('d')
        #описание куриного бульона какой он на вкус ,запах,как ты его ешь
        return True
    if f==3:
        print('s')
        #описание макарошек какие они на вкус ,запах,как ты его ешь
        return True
    if f==4:
        print('a')
        #описание пюрешки какая оня на вкус ,запах,как ты его ешь
        return True

sup()
