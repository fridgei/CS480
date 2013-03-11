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


def convert_tokens(token):
    if token.type == 'V_INT':
        token.value += ".0"
        token.type = 'V_REAL'
    elif token.type == 'OB_IFF':
        token.value = 'xor invert'
    elif token.type == 'OB_NOT':
        token.value = 'invert'
    return token


def tokenize(src):
    tokens = []
    for token in input_stream(src):
        for parser, token_type in parse_order:
            if re.search(parser, token):
                tokens.append(Token(token, token_type))
                break
    return map(convert_tokens, tokens)
