from flask import jsonify

from data_access.service.redis_service import RedisService
from data_access.service.mongodb_service import MongoDBService

class DBManager():
    def __init__(self):
        self.redis = RedisService()
        self.mongo = MongoDBService()

    def get(self, query: str):
        # TODO implement
        # get from redis
        # if miss from mongo
        #   if not miss at mongo: redis.insert (query -> recipe)
        # create response
        #   if miss from both: return error message: error_item_not_found(query)
        #   return formatted reponse, [200/400], add in [redis/mongodb] depending on where it came from
        # 
        
        
        pass
    
    def post(self, email: str, title: str, description: str, 
             tag1: str = None, tag2: str = None, tag3: str = None):
        # TODO implement
        # return response, [200/400]
        return jsonify({
            "message": "Worked!"
        })
        
        # TODO when you add an item to Redis, add it under all existing tags as well (0-3 tags) for better lookups
        pass
    
    
        # email: one word, max 100 chars,
        # title: max 100 chars,
        # tag1: one word, max 100 chars,
        # tag2: one word, max 100 chars,
        # tag3: one word, max 100 chars,
        # description: max 5000 chars
    
    def delete(self, item: str):
        # TODO implement
        # return response, [200/400]
        pass