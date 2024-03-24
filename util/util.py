def is_one_word(string: str):
    for c in string:
        if c.isspace():
            return False
    return True

def char_count(string: str):
    return len(string)

def strip_whitespace(string: str):
    return str.strip
