from DB.noteDB import noteDB
from datetime import datetime

class Note:
    def __init__(self):
        pass

    def show_note(self):
        print(noteDB.find(self))

    def add_note(self, title, content):
        date = datetime.today().strftime("%Y/%m/%d")
        noteDB.insert(self, title, content, date)
        print("추가되었습니다!")

    def delete_note(self, title):
        noteDB.delete(self, title)
        print("삭제되었습니다!")

    def update_note(self, title, mTitle, mContent):
        date = datetime.today().strftime("%Y/%m/%d")
        noteDB.delete(self, title)
        noteDB.insert(self, mTitle, mContent, date)
        print("수정되었습니다!")

    def __str__(self):
        pass

if __name__ == '__main__':
    note = Note()
    note.show_note()
