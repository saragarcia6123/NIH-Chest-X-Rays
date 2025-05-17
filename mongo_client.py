import os
from dotenv import load_dotenv

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

class MongoClient():

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance._initialize()
        return cls.instance

    def __init__(self):
        _uri = f"mongodb+srv://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}/?retryWrites=true&w=majority&appName={os.getenv('MONGODB_NAME')}"
        self.client = MongoClient(_uri, server_api=ServerApi('1'))

    def test_connection(self):
        try:
            client.admin.command('ping')
            print("Successfully connected to MongoDB!")
        except Exception as e:
            print(e)
    