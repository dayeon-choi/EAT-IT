from pymongo import MongoClient
from DB.DBHandler import DBHandler

class timerDB():
    # 연결
    my_client = MongoClient("mongodb://localhost:27017/")
    mydb = ""
    mycol = ""

    def __init__(self):
        dblist = timerDB.my_client.list_database_names()
        if "timerdb" in dblist:  # db가 존재한다면
            timerDB.mydb = timerDB.my_client["timerdb"]
            collist = timerDB.mydb.list_collection_names()
            if "timercol" in collist:  # collection 존재한다면
                timerDB.mycol = timerDB.mydb['timerdb']
                print("'timerdb' is already exists!")

        else:  # db가 존재하지 않다면
            # db 생성
            timerDB.mydb = timerDB.my_client['timerdb']
            timerDB.mycol = timerDB.mydb['timerdb']
            x = timerDB.mycol.insert_one({"time": "test", "date": "test"})

    def insert(self, time, date):
        DBHandler.insert_item_one(timerDB.my_client, {"title": time, "date": date}, "timerdb", "timercol")

    def delete(self, title):
        DBHandler.delete_item_one(timerDB.my_client, {"title": title}, "timerdb", "timercol")

    def find(self):
        list = DBHandler.find_item(timerDB.my_client, None, "timerdb", "timercol")
        dbListAll = []
        dbList = []
        for dic in list:
            for i in dic.values():
                dbList.append(i)
            dbListAll.append(dbList)
            dbList = []
        return dbListAll

    def __str__(self):
        list = DBHandler.find_item(timerDB.my_client, None, "timerdb", "timercol")
        for x in list:
            print(x)


if __name__ == '__main__':
    timerDB = timerDB()
    print(timerDB.find())