from app.util.util import get_logger
import redis
import json
from redis import exceptions
from redis.commands.json.path import Path

from app.settings import retrieve_redis_password, REDIS_HOST, REDIS_PORT, REDIS_DB, ITEM_TIMEOUT


class RedisService:
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        redis_password = retrieve_redis_password()
        if not redis_password:
            raise exceptions.AuthenticationError("Error: Unable to retrieve redis password from the environment")
        self.conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=redis_password, db=REDIS_DB, socket_connect_timeout=3)
        self.conn.ping()
        self.logger.info("Success: Connection established with Redis Cloud.")

    def get(self, item: str) -> dict | None:
        """
        Returns the value of item from the cache | None (if DNE)
        """
        result = self.conn.get(item)
        if (result):
            result = json.loads(result.decode('utf-8'))
        return result
    
    def set(self, item: str, value: dict) -> bool:
        '''
        Caches/updates item -> value
        '''
        value_json = json.dumps(value)
        is_set = self.conn.set(item, value_json)
        self.conn.expire(item, ITEM_TIMEOUT)
        return is_set
