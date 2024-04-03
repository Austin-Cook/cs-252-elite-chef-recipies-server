from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from util.util import get_logger
from settings import retrieve_mongodb_uri, MONGODB_DB_NAME, MONGODB_RECIPE_COLLECTION, EMAIL, TITLE, DESCRIPTION, TAG1, TAG2, TAG3


class MongoDBService:
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self.conn = MongoClient(retrieve_mongodb_uri(), server_api=ServerApi('1'))
        self.conn.admin.command('ping')
        self.logger.info("Success: Connection established with MongoDB Atlas.")
        self.db = self.conn.get_database(MONGODB_DB_NAME)
        self.recipies = self.db.get_collection(MONGODB_RECIPE_COLLECTION)

    def insert(self, email: str, title: str, description: str, 
             tag1: str = None, tag2: str = None, tag3: str = None) -> bool:
        insert_result =  self.recipies.insert_one({
            EMAIL: email,
            TITLE: title,
            DESCRIPTION: description,
            TAG1: tag1,
            TAG2: tag2,
            TAG3: tag3
        })
        if (insert_result.inserted_id):
            return True
        return False
    
    def find_one(self, item: str):
        filter = {
            "$or": [
                {TITLE: item},
                {TAG1: item},
                {TAG2: item},
                {TAG3: item}
            ]
        }
        return self.recipies.find_one(filter=filter, projection={'_id': 0})
        
    def delete_all_by_email(self, email: str) -> int:
        '''
        Returns the number of items deleted
        '''
        return self.recipies.delete_many({ EMAIL: email }).deleted_count
    