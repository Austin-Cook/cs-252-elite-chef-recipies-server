from data_access.service.redis_service import RedisService
from data_access.service.mongodb_service import MongoDBService
from util.response import response_error_unable_to_add_item_to_mongo, response_success_add_to_mongo, response_success_delete, response_success_find, response_error_no_matching_item
from settings import MONGODB_ATLAS, REDIS_CLOUD, TAG1, TAG2, TAG3

class DBManager():
    def __init__(self):
        self.redis = RedisService()
        self.mongo = MongoDBService()

    def get(self, item: str):
        # 1) check in Redis
        recipe = self.redis.get(item)
        if (recipe is not None):
            return response_success_find(recipe, REDIS_CLOUD)
        # 2) else check in MongoDB
        recipe = self.mongo.find_one(item)
        if (recipe is not None):
            # cache in Redis for faster lookups
            self.redis.set(item, recipe)
            if (recipe[TAG1] is not None):
                self.redis.set(recipe[TAG1], recipe)
            if (recipe[TAG2] is not None):
                self.redis.set(recipe[TAG2], recipe)
            if (recipe[TAG3] is not None):
                self.redis.set(recipe[TAG3], recipe)
            return response_success_find(recipe, MONGODB_ATLAS)
        # 3) no matching recipies in Mongo or Redis
        return response_error_no_matching_item(item)
    
    def post(self, email: str, title: str, description: str, 
             tag1: str = None, tag2: str = None, tag3: str = None):
        if (self.mongo.insert(email=email, title=title, description=description, 
                              tag1=tag1, tag2=tag2, tag3=tag3)):
            return response_success_add_to_mongo()
        return response_error_unable_to_add_item_to_mongo()
    
    def delete(self, email: str):
        return response_success_delete(self.mongo.delete_all_by_email(email))
