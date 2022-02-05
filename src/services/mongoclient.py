from typing import List
from pymongo import MongoClient
import os

class DbClient:
    def connect(self) -> MongoClient:
        host = os.getenv("MONGO_HOST")
        user = os.getenv("MONGO_USER")
        pwd  = os.getenv("MONGO_PWD")
        db   = os.getenv("MONGO_DB")
        
        conn_str = f"mongodb+srv://{user}:{pwd}@{host}/{db}?retryWrites=true&w=majority"
        client = MongoClient(conn_str)
        return client
        
    def load_data(self, input_data:List):
        return None