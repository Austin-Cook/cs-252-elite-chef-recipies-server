from settings import retrieve_redis_password, REDIS_HOST, REDIS_PORT, REDIS_DB
import redis

class RedisService:
    def __init__(self):
        # todo get commection
        redis_password = retrieve_redis_password()
        if not redis_password:
            raise Exception("Error: Unable to retrieve redis password from the environment")
        self.conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=redis_password, db=REDIS_DB, socket_connect_timeout=7)
        
    # TODO
    # def ...
    # def hi(self):
    #     result = self.conn.get("string")
    #     if result is None:
    #         ...
            
    #     self.conn.set(..., ...)
    
    # TODO when you add an item to Redis, add it under all existing tags as well (0-3 tags) for better lookups
    # TODO enforce 5000 char limit for description and 100 char limit for all else
    # TODO also add items 
