from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


class Phase(Enum):
    INPUT_FIRSTNAME = auto()
    INPUT_SURNAME = auto()
    INPUT_BORN = auto()
    DONE = auto()



@dataclass()
class PassportData:
    firstName: str
    surName: str
    born: datetime
    userId: str = "unknown"
    phase: Phase = Phase.INPUT_FIRSTNAME

    def __init__(self):
        self.userId = self.userId


def inputFirstName(data):
    if data.phase is not Phase.INPUT_FIRSTNAME:
        return
    data.firstName = input('введи своё имя\n')
    data.phase = Phase(data.phase.value+1)

def inputSurName(data):
    if data.phase is not Phase.INPUT_SURNAME:
        return
    data.surName = input('введи свою фамилия\n')
    data.phase = Phase(data.phase.value+1)


def printData(data):
    print(data)


def inputBorn(data):
    if data.phase is not Phase.INPUT_BORN:
        return
    try:
        dateStr = input('Введите дату рождения в формате дд.мм.гггг:\n')
        data.born = datetime.strptime(dateStr, '%d.%m.%Y')
        data.phase = Phase(data.phase.value+1)
    except ValueError:
        return


handlers = [inputFirstName, inputSurName, inputBorn]


def handeEvent(data):
    for handler in handlers:
        handler(data)
    if data.phase is Phase.DONE:
        return False
    else:
        return True


userData = PassportData()

i = 0
while handeEvent(userData):
    i += 1

printData(userData)
