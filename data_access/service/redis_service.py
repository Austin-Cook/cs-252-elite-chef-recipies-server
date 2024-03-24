from settings import retrieve_redis_password, REDIS_HOST, REDIS_PORT, REDIS_DB
from util.util import get_logger
from flask import json
import redis
from redis import exceptions


class RedisService:
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        redis_password = retrieve_redis_password()
        if not redis_password:
            raise exceptions.AuthenticationError("Error: Unable to retrieve redis password from the environment")
        self.conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=redis_password, db=REDIS_DB, socket_connect_timeout=7)
        self.conn.ping()
        self.logger.info("Success: Connection established with Redis Cloud.")

    def get(self, item):
        """
        Returns the value of item from the cache | None (if DNE)
        """
        return(self.conn.get(item))
    
    
    def set(self, item: str, value: json):
        '''
        Caches/updates item -> value
        '''
        return self.conn.set(item, value)
