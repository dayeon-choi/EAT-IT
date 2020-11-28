from DB.noteDB import noteDB
from datetime import datetime

class Note:
    def __init__(self):
        pass

    def show_note(self):
        print(noteDB.find(self))

    def add_note(self):
        title = input("제목 입력 : ")
        content = input("내용 입력 : ")
        date = datetime.today().strftime("%Y/%m/%d")
        noteDB.insert(self, title, content, date)
        print("추가되었습니다!")

    def delete_note(self):
        title = input("데이터베이스에 있는 노트의 제목을 입력하세요 : ")
        noteDB.delete(self, title)
        print("삭제되었습니다!")

    def update_note(self):
        modify_title = input("수정할 노트의 제목을 입력하세요 : ")
        title = input("수정한 제목을 입력하세요 : ")
        content = input("수정한 내용을 입력하세요 : ")
        date = datetime.today().strftime("%Y/%m/%d")
        noteDB.update(self, modify_title, title, content, date)
        print("수정되었습니다!")

    def __str__(self):
        pass

if __name__ == '__main__':
    note = Note()
    note.show_note()
