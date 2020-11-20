from pymongo import MongoClient
from DB.DBHandler import DBHandler

# 연결
my_client = MongoClient("mongodb://localhost:27017/")

class noteDB():
    mydb = ""
    mycol = ""

    def __init__(self):
        dblist = my_client.list_database_names()
        if "notedb" in dblist:  # db가 존재한다면
            my_db = my_client["notedb"]
            noteDB.mydb = my_db
            collist = noteDB.mydb.list_collection_names()
            if "notecol" in collist:  # collection 존재한다면
                noteDB.mycol = noteDB.mydb['notecol']
                print("'notecol' is already exists!")

        else:  # db가 존재하지 않다면
            # db 생성
            mydb = my_client['notedb']
            mycol = mydb['notecol']
            x = mycol.insert_one({"title": "test", "content": "test", "date":"test"})

    def insert(self, title, content, date):
        # 수정
        DBHandler.insert_item_many(my_client, {"title": title, "content": content, "date": date}, "notedb", "notecol")

    def update(self):
        DBHandler.update_item_one()

    def delete(self):
        DBHandler.delete_item_one()

    def __str__(self):
        list = noteDB.mycol.find()
        for x in list:
            print(x)

if __name__ == '__main__':
    noteDB = noteDB()
