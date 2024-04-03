# elite-chef-recipies-server

## Run
Run with `python3 elite_chef_recipies_server.py`

## Endpoints

### GET /recipe
Retrieve a recipe from the database  
- Request
```
{
    query: one word, max 100 characters
}
```
- Success Response
```
{
    message: ...,
    retrieved_from: [redis/mongodb],
    email: ...,
    title: ...,
    tag1: ...,
    tag2: ...,
    tag3: ...,
    description: ...
}, 200
```
- Error Response
```
{
    message: ...
}, 400
```

### POST /recipe
Post a new recipe to the database  
- Request
```
{
    message: ...,
    email: one word, max 100 chars,
    title: max 100 chars,
    tag1 (optional): one word, max 100 chars,
    tag2 (optional): one word, max 100 chars,
    tag3 (optional): one word, max 100 chars,
    description: max 5000 chars
}
```
- Success Response
```
{
    message: ...
}, 200
```
- Error Response
```
{
    message: ...
}, 400
```

### DELETE /recipe
Delete all recipes in the database created by the user  
- Request
```
{
    email: one word, max 100 chars
}
```
- Success Response
```
{
    message: ...
}, 200
```
- Error Response
```
{
    message: ...
}, 400
```

## System Details
### Overview
- Uses Cache-Aside Strategy
    - First check the Redis cache
    - If a miss, check the MongoDB database
        - If in MongoDB, cache result in Redis

### MongoDB


### Redis
- Uses Cache-Aside Strategy
- Remove items by LRU (least recently used)
- Cache the recipe:
    - recipe_title -> recipe_data
    - tag# -> recipe_data (for all tags)

### Front-End
- React Application

### Server
- Python Flask Rest API Server