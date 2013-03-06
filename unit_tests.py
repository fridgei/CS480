import unittest
from tokenizer import input_stream, tokenize
from tokens import parse_order, Token
from itertools import izip
from combinator import *

class TokenizerTest(unittest.TestCase):

    def test_add_value(self):
        test_str = "(+ (- 234 1) 23)"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("+", "O_ADD"),
                           Token("(", "L_PAREN"),
                           Token("-", "O_SUB"),
                           Token("234", "V_INT"),
                           Token("1", "V_INT"),
                           Token(")", "R_PAREN"),
                           Token("23", "V_INT"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        print consumed
        print remaining
        #self.assertEqual(remaining, [])
        print code_generate(remaining)
        if not remaining:
            print "accepted"
            print consumed


if __name__ == '__main__':
    unittest.main()
