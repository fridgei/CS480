import unittest
from tokenizer import input_stream, tokenize
from tokens import parse_order, Token
from itertools import izip
from combinator import *

class TokenizerTest(unittest.TestCase):

    def test_real_value(self):
        test_str = "(assign turds 234.234)"
        expected_tokens = [Token("(", 'L_PAREN'),
                           Token("assign", 'E_ASSIGN'),
                           Token("turds", 'V_STRING'),
                           Token("234.234", 'V_REAL'),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        print actual_tokens
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed


    def test_int_value(self):
        test_str = "(assign turds 234)"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("assign", "E_ASSIGN"),
                           Token("turds", "V_STRING"),
                           Token("234", "V_INT"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed

    def test_add_value(self):
        test_str = "(+ 234 234.123)"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("+", "O_ADD"),
                           Token("234", "V_INT"),
                           Token("234.123", "V_REAL"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed

    def test_while(self):
        test_str = "(while (< 3 i) (assign i (+ i 1)))"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("while", "E_WHILE"),
                           Token("(", "L_PAREN"),
                           Token("<", "O_LT"),
                           Token("3", "V_INT"),
                           Token("i", "V_STRING"),
                           Token(")", "R_PAREN"),
                           Token("(", "L_PAREN"),
                           Token("assign", "E_ASSIGN"),
                           Token("i", "V_STRING"),
                           Token("(", "L_PAREN"),
                           Token("+", "O_ADD"),
                           Token("i", "V_STRING"),
                           Token("1", "V_INT"),
                           Token(")", "R_PAREN"),
                           Token(")", "R_PAREN"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed

    def test_let_value(self):
        test_str = "(let ((a int)(b real)))"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("let", "E_LET"),
                           Token("(", "L_PAREN"),
                           Token("(", "L_PAREN"),
                           Token("a", "V_STRING"),
                           Token("int", "T_INT"),
                           Token(")", "R_PAREN"),
                           Token("(", "L_PAREN"),
                           Token("b", "V_STRING"),
                           Token("real", "T_REAL"),
                           Token(")", "R_PAREN"),
                           Token(")", "R_PAREN"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed


    def test_div(self):
        test_str = "(* (\ 8 2) 2)"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("*", "O_MUL"),
                           Token("(", "L_PAREN"),
                           Token("\\", "O_DIV"),
                           Token("8", "V_INT"),
                           Token("2", "V_INT"),
                           Token(")", "R_PAREN"),
                           Token("2", "V_INT"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed

    def test_final_boss(self):
        test_str = "(if (< 3 5) (println \"hello\"))"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("if", "E_IF"),
                           Token("(", "L_PAREN"),
                           Token("<", "O_LT"),
                           Token("3", "V_INT"),
                           Token("5", "V_INT"),
                           Token(")", "R_PAREN"),
                           Token("(", "L_PAREN"),
                           Token("println", "E_PRINT"),
                           Token("\"hello\"", "V_STRING"),
                           Token(")", "R_PAREN"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertEqual(remaining, [])
        if not remaining:
            print "accepted"
            print consumed


    def test_final_boss2(self):
        test_str = "(if (< 3 5) println \"hello\"))"
        expected_tokens = [Token("(", "L_PAREN"),
                           Token("if", "E_IF"),
                           Token("(", "L_PAREN"),
                           Token("<", "O_LT"),
                           Token("3", "V_INT"),
                           Token("5", "V_INT"),
                           Token(")", "R_PAREN"),
                           Token("println", "E_PRINT"),
                           Token("\"hello\"", "V_STRING"),
                           Token(")", "R_PAREN"),
                           Token(")", "R_PAREN")]
        actual_tokens = tokenize(test_str)
        for actual, expected in izip(actual_tokens, expected_tokens):
            self.assertEqual(actual, expected)
        consumed, remaining = S(actual_tokens)
        self.assertNotEqual(remaining, [])
        if remaining:
            print "rejected at {0}".format(remaining[0])
if __name__ == '__main__':
    unittest.main()
