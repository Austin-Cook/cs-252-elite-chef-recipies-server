from flask import Request
from data_access.db_manager import DBManager
from util.util import *
from util.errors import *

QUERY = "query"
EMAIL = "email"
TITLE = "title"
TAG1 = "tag1"
TAG2 = "tag2"
TAG3 = "tag3"
DESCRIPTION = "description"


class QueryHandler:
    def __init__(self):
        self.db_manager = DBManager()

    def process_get(self, request: Request):
        # validate input
        if not request.is_json:
            return error_not_json, 400
        if not QUERY in request.json:
            return error_missing_field(QUERY), 400
        if not isinstance(request.json[QUERY], str):
            return error_wrong_type(QUERY), 400
        query = strip_whitespace(request.json[QUERY])
        length = char_count(query)
        if (length > 100):
            return error_field_too_large(query, 100, length), 400      
        
        return self.db_manager.get(query)
        

    def process_post(self, request: Request):
        # validate input
        if not request.is_json:
            return jsonify(error_not_json), 400
        if not EMAIL in request.json:
            return error_missing_field(QUERY), 400
        if not TITLE in request.json:
            return error_missing_field(TITLE), 400
        if not DESCRIPTION in request.json:
            return error_missing_field(DESCRIPTION), 400
        
        # TODO this should all be done at one place!!! WHERE TO DO THIS
        
        # email: one word, max 100 chars,
        # title: max 100 chars,
        # tag1: one word, max 100 chars,
        # tag2: one word, max 100 chars,
        # tag3: one word, max 100 chars,
        # description: max 5000 chars

        
        return self.db_manager.post("request.json")

    def process_delete(self, request: Request):
        # validate input
        if not request.is_json:
            return jsonify(error_not_json), 400
        if not EMAIL in request.json:
            return error_missing_field(QUERY), 400
        if not isinstance(request.json[EMAIL], str):
            return error_wrong_type(EMAIL), 400
        email = strip_whitespace(request.json[EMAIL])
        length = char_count(email)
        if (length > 100):
            return error_field_too_large(email, 100, length), 400
        
        return self.db_manager.delete(email)
