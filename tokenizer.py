from itertools import dropwhile
import re
from tokens import parse_order, Token


def input_stream(src):
    token = ""
    for char in dropwhile(lambda x: x in '\t\n', src):
        if char in '+-\\*()=><%^' and token:
            yield token
            yield char
            token = ""
        elif char is ' ' and token:
            yield token
            token = ""
        elif char is ' ':
            continue
        else:
            token += char
    yield token


def tokenize(src):
    tokens = []
    for token in input_stream(src):
        for parser, token_type in parse_order:
            if re.search(parser, token):
                tokens.append(Token(token, token_type))
                break
    return tokens
