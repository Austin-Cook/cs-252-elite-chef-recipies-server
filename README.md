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
- Primary database to store recipies

### Redis
- Uses Cache-Aside Strategy
- Item Removal:
    - LRU (least recently used)
    - Timout (currently set to 1 day)
- Cache the recipe:
    - recipe_title -> recipe_data
    - tag# -> recipe_data (for all tags)

### Front-End
- React Application

### Server
- Python Flask Rest API Server

### Things to Work Out
- Because Redis items are set to expire on a timer, deleting a user's posts from MongoDB won't be reflected in query results until the cooresponding Redis entry times out or is pushed out.
