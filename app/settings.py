import os
import logging

LOG_LEVEL = logging.DEBUG

# GENERAL

QUERY_MAX_LEN = 100
EMAIL_MAX_LEN = 100
TITLE_MAX_LEN = 100
TAG_MAX_LEN = 100
DESCRIPTION_MAX_LEN = 5000
RETRIEVED_FROM = "retrieved_from"
MONGODB_ATLAS = "MongoDB Atlas"
REDIS_CLOUD = "Redis Cloud"
MESSAGE = "message"
QUERY = "query"
EMAIL = "email"
TITLE = "title"
TAG1 = "tag1"
TAG2 = "tag2"
TAG3 = "tag3"
DESCRIPTION = "description"

# REDIS

REDIS_HOST = "redis-19367.c299.asia-northeast1-1.gce.cloud.redislabs.com"
REDIS_PORT = 19367
REDIS_DB = 0
def retrieve_redis_password() -> str:
    redis_password =  os.environ.get('REDIS_CLOUD_PASSWORD')
    if (redis_password is None):
        raise KeyError("Unable to locate REDIS_CLOUD_PASSWORD in the environment. Add `export REDIS_CLOUD_PASSWORD={PASSWORD}` to the bottom of `~/.bashrc`")
    return redis_password
ITEM_TIMEOUT = 86400 # 1 day

# MONGODB

MONGODB_USERNAME = "cluster_0_user"
MONGODB_CONN_STRING = "mongodb+srv://{}:{}@cluster0.8tpshhm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
def retrieve_mongodb_uri() -> str:
    MONGODB_PASSWORD = os.environ.get('MONGODB_ATLAS_PASSWORD')
    if (MONGODB_PASSWORD is None):
        raise KeyError("Unable to locate MONGODB_ATLAS_PASSWORD in the environment. Add `export MONGODB_ATLAS_PASSWORD={PASSWORD}` to the bottom of `~/.bashrc`")
    return MONGODB_CONN_STRING.format(MONGODB_USERNAME, MONGODB_PASSWORD)
MONGODB_DB_NAME = "eliteChefRecipiesDB"
MONGODB_RECIPE_COLLECTION = "recipies"
