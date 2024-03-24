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
             tag1: str = None, tag2: str = None, tag3: str = None):
        return self.recipies.insert({
            EMAIL: email,
            TITLE: title,
            DESCRIPTION: description,
            TAG1: tag1,
            TAG2: tag2,
            TAG3: tag3
        })
    
    def find_one_by_title(self, title: str):
        filter = {
            TITLE: title
        }
        projection = {
            # TODO MAKE SURE THIS DOESN'T EXCLUDE THE OTHER FIELDS
            "_id": 0
        }
        return self.recipies.find().limit(1)[0] # TODO MAKE SURE I ACCESS THE ARRAY PROPERLY
        
    def delete_all_by_email(self, email: str):
        return self.recipies.delete_many({ EMAIL: email })
    