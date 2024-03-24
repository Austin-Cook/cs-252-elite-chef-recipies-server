import os

QUERY_MAX_LEN, EMAIL_MAX_LEN, TITLE_MAX_LEN, TAG_MAX_LEN = 100
DESCRIPTION_MAX_LEN = 5000

QUERY = "query"
EMAIL = "email"
TITLE = "title"
TAG1 = "tag1"
TAG2 = "tag2"
TAG3 = "tag3"
DESCRIPTION = "description"

REDIS_HOST = "redis-19367.c299.asia-northeast1-1.gce.cloud.redislabs.com"
REDIS_PORT = 19367
REDIS_DB = 0
def retrieve_redis_password():
    return os.environ.get('REDIS_CLOUD_PASSWORD')
