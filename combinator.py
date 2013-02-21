from tokens import Token
from base_parsers import L_PAREN, R_PAREN, ATOM, EPSILON


def or_combinator(parsers):
    def combinator(tokens_to_match):
        for _parser in parsers:
            # This is a hack I will figure out a better solution another time
            try:
                consumed, remaining = _parser(tokens_to_match)
            except TypeError:
                consumed, remaining = _parser()(tokens_to_match)
            if consumed != None:
                return consumed, remaining
        return None, tokens_to_match
    return combinator


def and_combinator(parsers):
    def parse(tokens_to_match):
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
            rule_consumed += consumed if type(consumed) == list else [consumed]
        return rule_consumed, remaining
    return parse

# S  => (S1 | ATOM S2
# S1 => )S2 | S)S2
# S2 => S | epsilon

S = lambda: or_combinator([and_combinator([L_PAREN, S1]), and_combinator([ATOM, S2])])
S1 = lambda: or_combinator([and_combinator([R_PAREN, S2]), and_combinator([S, R_PAREN, S2])])
S2 = lambda: or_combinator([S, EPSILON])

S = S()
S1 = S1()
S2 = S2()
