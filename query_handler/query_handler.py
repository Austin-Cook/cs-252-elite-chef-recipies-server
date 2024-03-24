from flask import Request
from data_access.db_manager import DBManager
from util.util import strip_whitespace, char_count
from util.errors import error_not_json, error_field_missing, error_field_empty, error_field_too_large, error_wrong_type
from settings import QUERY_MAX_LEN, EMAIL_MAX_LEN, TITLE_MAX_LEN, TAG_MAX_LEN, DESCRIPTION_MAX_LEN, QUERY, EMAIL, TITLE, TAG1, TAG2, TAG3, DESCRIPTION


class QueryHandler:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def process_get(self, request: Request):
        if not request.is_json:
            return error_not_json(), 400
        if not QUERY in request.json:
            return error_field_missing(QUERY), 400
        if not isinstance(request.json[QUERY], str):
            return error_wrong_type(QUERY), 400
        query = strip_whitespace(request.json[QUERY])
        len = char_count(query)
        if (len == 0):
            return error_field_empty(QUERY)
        if (len > QUERY_MAX_LEN):
            return error_field_too_large(QUERY, QUERY_MAX_LEN, len), 400      
        
        return self.db_manager.get(query)
        

    def process_post(self, request: Request):
        if not request.is_json:
            return error_not_json(), 400
        json = request.json
        if not EMAIL in json:
            return error_field_missing(EMAIL), 400
        if not TITLE in json:
            return error_field_missing(TITLE), 400
        if not DESCRIPTION in json:
            return error_field_missing(DESCRIPTION), 400
        if not isinstance(json[EMAIL], str):
            return error_wrong_type(EMAIL), 400
        if not isinstance(json[TITLE], str):
            return error_wrong_type(TITLE), 400
        if not isinstance(json[DESCRIPTION], str):
            return error_wrong_type(DESCRIPTION), 400
        email = strip_whitespace(json[EMAIL])
        title = strip_whitespace(json[TITLE])
        description = strip_whitespace(json[DESCRIPTION])
        email_len = char_count(email)
        title_len = char_count(title)
        description_len = char_count(description)
        if (email_len == 0):
            return error_field_empty(EMAIL)
        if (title_len == 0):
            return error_field_empty(TITLE)
        if (description_len == 0):
            return error_field_empty(DESCRIPTION)
        if (email_len > EMAIL_MAX_LEN):
            return error_field_too_large(EMAIL, EMAIL_MAX_LEN, email_len)
        if (title_len > TITLE_MAX_LEN):
            return error_field_too_large(TITLE, TITLE_MAX_LEN, title_len)
        if (description_len > DESCRIPTION_MAX_LEN):
            return error_field_too_large(DESCRIPTION, DESCRIPTION_MAX_LEN, description_len)
        # tags of len 0 are not used
        tag1 = None
        tag2 = None
        tag3 = None
        tag = json.get(TAG1)
        if tag is not None:
            if not isinstance(tag, str):
                return error_wrong_type(TAG1), 400
            tag = strip_whitespace(tag)
            len = char_count(tag)
            if len > TAG_MAX_LEN:
                return error_field_too_large(TAG1, TAG_MAX_LEN, len)
            if len > 0:
                tag1 = tag
        tag = json.get(TAG2)
        if tag is not None:
            if not isinstance(tag, str):
                return error_wrong_type(TAG2), 400
            tag = strip_whitespace(tag)
            len = char_count(tag)
            if len > TAG_MAX_LEN:
                return error_field_too_large(TAG2, TAG_MAX_LEN, len)
            if len > 0:
                tag2 = tag
        tag = json.get(TAG3)
        if tag is not None:
            if not isinstance(tag, str):
                return error_wrong_type(TAG3), 400
            tag = strip_whitespace(tag)
            len = char_count(tag)
            if len > TAG_MAX_LEN:
                return error_field_too_large(TAG3, TAG_MAX_LEN, len)
            if len > 0:
                tag3 = tag
        
        return self.db_manager.post(email=email, title=title, description=description, 
                                    tag1=tag1, tag2=tag2, tag3=tag3)

    def process_delete(self, request: Request):
        if not request.is_json:
            return error_not_json(), 400
        if not EMAIL in request.json:
            return error_field_missing(QUERY), 400
        if not isinstance(request.json[EMAIL], str):
            return error_wrong_type(EMAIL), 400
        email = strip_whitespace(request.json[EMAIL])
        len = char_count(email)
        if (len == 0):
            return error_field_empty(EMAIL)
        if (len > EMAIL_MAX_LEN):
            return error_field_too_large(EMAIL, EMAIL_MAX_LEN, len), 400
        
        return self.db_manager.delete(email)
