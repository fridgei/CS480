from tokens import Token
from base_parsers import L_PAREN, R_PAREN, ATOM, EPSILON


def case_combinator(parsers):
    def combinator(tokens_to_match):
        for _parser in parsers:
            try:
                consumed, remaining = _parser(tokens_to_match)
            except TypeError:
                consumed, remaining = _parser()(tokens_to_match)
            if consumed != None:
                return consumed, remaining
        return None, tokens_to_match
    return combinator


def parser_combinator(parsers):
    def parse(tokens_to_match):
        tokens_remaining = tokens_to_match
        consumed = []
        for _parse in parsers:
            try:
                tokens_consumed, tokens_remaining = _parse(tokens_remaining)
            except TypeError:
                tokens_consumed, tokens_remaining = _parse()(tokens_remaining)
            if tokens_consumed == None:
                return None, tokens_to_match
            elif type(tokens_consumed) == list:
                consumed = tokens_consumed + consumed
            else:
                consumed = [tokens_consumed] + consumed
        return consumed, tokens_remaining
    return parse

# S  => (S1 | ATOM S2
# S1 => )S2 | S)S2
# S2 => S | epsilon

# disregard the lambda.  Its a lazy hack.
S = lambda: or_combinator([and_combinator([L_PAREN, S1]), and_combinator([ATOM, S2])])
S1 = lambda: or_combinator([and_combinator([R_PAREN, S2]), and_combinator([S, R_PAREN, S2])])
S2 = lambda: or_combinator([S, EPSILON])

S = S()
S1 = S1()
S2 = S2()

fail = [Token('', 'L_PAREN'), Token('', 'V_INT'), Token('', 'R_PAREN'), Token('', 'R_PAREN')]
not_fail = [Token('', 'L_PAREN'), Token('', 'V_REAL'), Token('', 'V_STRING'), Token('', 'V_INT'), Token('', 'R_PAREN')]
# QED 8====D
# thats a smiley face with a long nose
