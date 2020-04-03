from dataclasses import dataclass


@dataclass
class sups:
    d: str
    c: str


supchik = ['борщь', 'куриный бульон','макарошки', 'пюрешка']


def sup():
    d = input('какой суп вам приготовить?\n           меню          \n1.борщь \n2.куриный бульон \nчто вы выбрали?\n')
    c = input('что вам приготовить?посмотрите наше меню\n        меню       \n1.макарошки  \n2.пюрешка \nчто закажете?')
    f = supchik.index(d)


sup()
