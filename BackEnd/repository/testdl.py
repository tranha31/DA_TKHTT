from .dlbase import DLBase

class TestDL(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def TestConnect(self):
        sql = "Select * from admin"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall()
        return records

    def TestMongo(self):
        collection = self.dbMongo["test"]
        post = {"_id": 0, "name": "test"}
        collection.insert_one(post)