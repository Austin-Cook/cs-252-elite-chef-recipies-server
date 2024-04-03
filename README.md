# elite-chef-recipies-server

## Run
Run with `python3 elite_chef_recipies_server.py`

## Endpoints

### GET /recipe?query=QUERY
Retrieve a recipe from the database  
query: one word, max 100 characters
- Request
```
Empty
```
- Success Response
```
{
    message: ...,
    retrieved_from: [redis/mongodb],
    email: ...,
    title: ...,
    tag1: ..., // Optional
    tag2: ..., // Optional
    tag3: ..., // Optional
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
}, 500
```

### DELETE /recipe?email=EMAIL
Delete all recipes in the database created by the user  
email: one word, max 100 chars
- Request
```
Empty
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

### Things to Work Out
- Redis items are set to expire on a timer. However, when we delete a user's recipies form MongoDB, we don't clear the cache so recipies will still temporarily show up in a search, even after deletion.
