import unittest
from tokenizer import input_stream, tokenize
from tokens import parse_order, Token
from itertools import izip
from combinator import *

class TokenizerTest(unittest.TestCase):

    def test_add_value(self):
        test_str = "(+ (- 234.3 1.1) 23)"
        actual_tokens = tokenize(test_str)
        consumed, remaining = S(actual_tokens)
        if not remaining:
            print "accepted"
            print consumed
        code = generate_code(consumed)
        print code


    def test_sin(self):
        test_str = "(sin 3.2)"
        actual_tokens = tokenize(test_str)
        consumed, remaining = S(actual_tokens)
        if not remaining:
            print "accepted"
            print consumed
        code = generate_code(consumed)
        print code


    def test_sin(self):
        test_str = "(sin 3.2)"
        actual_tokens = tokenize(test_str)
        consumed, remaining = S(actual_tokens)
        if not remaining:
            print "accepted"
            print consumed
        code = generate_code(consumed)
        print code


    def test_bool_value(self):
        test_str = "(and (or true false) true)"
        actual_tokens = tokenize(test_str)
        consumed, remaining = S(actual_tokens)
        if not remaining:
            print "accepted"
            print consumed
        code = generate_code(consumed)
        print code

    def test_iff(self):
        test_str = "(iff (and true false) false)"
        actual_tokens = tokenize(test_str)
        consumed, remaining = S(actual_tokens)
        if not remaining:
            print "accepted"
            print consumed
        code = generate_code(consumed)
        print code

    def test_not(self):
        test_str = "(not (and true false))"
        actual_tokens = tokenize(test_str)
        consumed, remaining = S(actual_tokens)
        if not remaining:
            print "accepted"
            print consumed
        code = generate_code(consumed)
        print code

if __name__ == '__main__':
    unittest.main()
