from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


class Phase(Enum):
    INPUT_FIRSTNAME = auto()
    INPUT_SURNAME = auto()
    INPUT_BORN = auto()


@dataclass()
class PassportData:
    firstName: str
    surName: str
    born: datetime
    userId: str = "unknown"
    phase: Phase = Phase.INPUT_FIRSTNAME

    def __init__(self):
        self.userId = self.userId


def inputName(data):
    data.firstName = input('введи своё имя\n')
    data.phase = Phase.INPUT_SURNAME


def inputSurName(data):
    data.surName = input('введи свою фамилия\n')
    data.phase = Phase.INPUT_BORN


def printData(data):
    print(data)


def inputBorn(data):
    try:
        dateStr = input('Введите дату рождения в формате дд.мм.гггг:\n')
        data.born = datetime.strptime(dateStr, '%d.%m.%Y')
        return False
    except ValueError:
        return True


def handeEvent(data):
    if data.phase is Phase.INPUT_FIRSTNAME:
        inputName(data)
    if data.phase is Phase.INPUT_SURNAME:
        inputSurName(data)
    if data.phase is Phase.INPUT_BORN:
        return inputBorn(data)
    return True


userData = PassportData()

i = 0
while handeEvent(userData):
    i += 1

printData(userData)