from DB.timerDB import timerDB
from datetime import datetime

class Timer:
    def __init__(self):
        pass

    def show_time(self):
        print(timerDB.find(self))

    def add_time(self, time):
        date = datetime.today().strftime("%Y/%m/%d")
        timerDB.insert(self, time, date)
        print("추가되었습니다!")

    def __str__(self):
        pass

if __name__ == '__main__':
    timer = Timer()
    timer.show_note()
