from app.data_access.service.redis_service import RedisService
from app.data_access.service.mongodb_service import MongoDBService
from app.util.response import res_err_unable_to_add_to_mongo, res_ok_add, res_ok_delete, resp_ok_find, res_err_no_matching_item
from app.settings import MONGODB_ATLAS, REDIS_CLOUD, TITLE, TAG1, TAG2, TAG3

class DBManager():
    def __init__(self):
        self.redis = RedisService()
        self.mongo = MongoDBService()

    def get(self, item: str):
        # 1) check in Redis
        recipe = self.redis.get(item)
        if (recipe is not None):
            return resp_ok_find(recipe, REDIS_CLOUD)
        # 2) else check in MongoDB
        recipe = self.mongo.find_one(item)
        if (recipe is not None):
            # cache in Redis for faster lookups
            if (recipe[TITLE] is not None):
                self.redis.set(recipe[TITLE], recipe)
            if (recipe[TAG1] is not None):
                self.redis.set(recipe[TAG1], recipe)
            if (recipe[TAG2] is not None):
                self.redis.set(recipe[TAG2], recipe)
            if (recipe[TAG3] is not None):
                self.redis.set(recipe[TAG3], recipe)
            return resp_ok_find(recipe, MONGODB_ATLAS)
        # 3) no matching recipies in Mongo or Redis
        return res_err_no_matching_item(item)
    
    def post(self, email: str, title: str, description: str, 
             tag1: str = None, tag2: str = None, tag3: str = None):
        if (self.mongo.insert(email=email, title=title, description=description, 
                              tag1=tag1, tag2=tag2, tag3=tag3)):
            return res_ok_add()
        return res_err_unable_to_add_to_mongo()
    
    def delete(self, email: str):
        return res_ok_delete(self.mongo.delete_all_by_email(email))
