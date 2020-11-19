from pymongo import MongoClient
from pymongo.cursor import CursorType

host = "localhost"
port = "27017"
mongo = MongoClient(host, int(port))
print(mongo)