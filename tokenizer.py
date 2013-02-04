from itertools import dropwhile
import re
from tokens import parse_order, Token
from collections import defaultdict
import sys

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
    yield token


def tokenize(src):
    symbol_table = {}
    tokens = []
    for token in input_stream(src):
        for parser, token_type in parse_order:
            if re.search(parser, token):
                t = Token(token, token_type)
                if not (token in symbol_table.keys()):
                    symbol_table[token] = t
                tokens.append(t)
                break
    return tokens, symbol_table

if __name__ == '__main__':
    with open(sys.argv[-1], 'r') as f:
        tokens, table = tokenize(f.read())
        print str(tokens)


