from pymongo import MongoClient
from DB.DBHandler import DBHandler

class noteDB():
    # 연결
    my_client = MongoClient("mongodb://localhost:27017/")
    mydb = ""
    mycol = ""

    def __init__(self):
        dblist = noteDB.my_client.list_database_names()
        if "notedb" in dblist:  # db가 존재한다면
            noteDB.mydb = noteDB.my_client["notedb"]
            collist = noteDB.mydb.list_collection_names()
            if "notecol" in collist:  # collection 존재한다면
                noteDB.mycol = noteDB.mydb['notecol']
                print("'notecol' is already exists!")

        else:  # db가 존재하지 않다면
            # db 생성
            noteDB.mydb = noteDB.my_client['notedb']
            noteDB.mycol = noteDB.mydb['notecol']
            x = mycol.insert_one({"title": "test", "content": "test", "date": "test"})

    def insert(self, title, content, date):
        DBHandler.insert_item_one(noteDB.my_client, {"title": title, "content": content, "date": date}, "notedb", "notecol")

    def update(self):
        DBHandler.update_item_one()

    def delete(self, title):
        DBHandler.delete_item_one(noteDB.my_client, {"title": title}, "notedb", "notecol")

    def __str__(self):
        list = DBHandler.find_item(noteDB.my_client, None, "notedb", "notecol")
        for x in list:
            print(x)

if __name__ == '__main__':
    noteDB = noteDB()
    noteDB.__str__()
