from itertools import dropwhile
import re
from tokens import parse_order, Token


def input_stream(src):
    token = ""
    for char in dropwhile(lambda x: x in '\t\n', src):
        if char in '+-\\*()=><%^':
            if token:
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


def tokenize(src):
    tokens = []
    for token in input_stream(src):
        for parser, token_type , gforth_repr in parse_order:
            if re.search(parser, token):
                tokens.append(Token(token, token_type, gforth_repr))
                break
    return tokens
