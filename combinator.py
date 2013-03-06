from tokens import Token, operator_table
from base_parsers import L_PAREN, R_PAREN, E1, E2, B1, B2, BOOL, NUM, EPSILON


def or_combinator(parsers):
    def parser(tokens_to_match):
        for _parser in parsers:
            # This is a hack I will figure out a better solution another time
            try:
                consumed, remaining = _parser(tokens_to_match)
            except TypeError:
                consumed, remaining = _parser()(tokens_to_match)
            if consumed != None:
                return consumed, remaining
        return None, tokens_to_match
    return parser


def and_combinator(parsers):
    def parser(tokens_to_match):
        remaining = tokens_to_match
        rule_consumed = []
        for _parse in parsers:
            # Same hack different function
            try:
                consumed, remaining = _parse(remaining)
            except TypeError:
                consumed, remaining = _parse()(remaining)
            if consumed == None:
                return None, tokens_to_match
            rule_consumed += consumed
        return rule_consumed, remaining
    return parser

S = lambda: or_combinator([and_combinator([L_PAREN, S1]),
                           and_combinator([ATOM, S2])])
S1 = lambda: or_combinator([and_combinator([R_PAREN, S2]),
                            and_combinator([E, R_PAREN, S2])])
S2 = lambda: or_combinator([S, EPSILON])
E = lambda: or_combinator([and_combinator([E1, S]),
                           and_combinator([E2, S, S]),
                           and_combinator([B1, S]),
                           and_combinator([B2, S, S])])

ATOM = lambda: or_combinator([BOOL, NUM])
S = S()
S1 = S1()
S2 = S2()
E = E()
ATOM = ATOM()

# S    => (ES`
# S`   => )S`` | S)S``
# S``  => S | EPSILON
# E    => E` N | E`` N N | B` BOOL | B`` BOOL BOOL
# E`   => NEGATE | SIN | COS | TAN | EXP
# E``  => PLUS | MINUS | TIMES | DIVIDE | REMAINDER | POWER | LT | EQ
# BOOL => TRUE | FALSE
# N    => FLOAT | INT

def code_generate(tokens):
    stack = []
    for token in tokens:
        if token.type not in ['L_PAREN', 'R_PAREN']:
            if token.type.startswith('V'):
                stack.append(token.value)
            else:
                stack.append(operator_table[token.type])
    stack.reverse()
    return stack
