from typing import List
from pymongo import MongoClient

class DbClient:
    def connect(self) -> MongoClient:
        client = MongoClient("mongodb+srv://root:Ynov44@gaspredict.a8svh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return client
        
    def load_data(self, input_data:List):
        return None