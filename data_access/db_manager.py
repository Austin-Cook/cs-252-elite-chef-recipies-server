from service.redis_service import RedisService
from service.mongodb_service import MongoDBService
from flask import json

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
    
    def post(self, request_json: json):
        # TODO implement
        # return response, [200/400]
        pass
    
    def delete(self, item: str):
        # TODO implement
        # return response, [200/400]
        pass