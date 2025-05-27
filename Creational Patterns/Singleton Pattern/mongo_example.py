from pymongo import MongoClient  # type: ignore


class MongoDBClient:
    _instance = None

    def __new__(cls, uri="mongodb://localhost:27017", db_name="mydb"):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._client = MongoClient(uri)
            cls._instance._db = cls._instance._client[db_name]
        return cls._instance

    def get_db(self):
        return self._db


# connection pooling
client1 = MongoDBClient()
client2 = MongoDBClient()

print(client1 is client2)  # True

db = client1.get_db()

# Second connection string will be ignored !!!

client1 = MongoDBClient(uri="mongodb://localhost:27017", db_name="mydb")
client2 = MongoDBClient(uri="mongodb://anotherhost:27018", db_name="otherdb")
