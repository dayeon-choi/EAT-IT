from DB.noteDB import noteDB

class Note:
    def __init__(self):
        self.add_note()

    def show_note(self):
        pass

    def add_note(self):
        title = input("제목 입력 : ")
        content = input("내용 입력 : ")
        date = input("날짜 아무거나 입력해봐 : ")
        noteDB.insert(title, content, date)
        print("추가되었습니다!")

    def delete_note(self):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    note = Note()
    note.add_note()
