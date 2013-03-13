from tokens import Token
from base_parsers import L_PAREN, R_PAREN, E1, E2, B1, B2, ATOM, EPSILON


def or_combinator(parsers):
    def parser(tokens_to_match):
        for _parser in parsers:
            try:
                consumed, remaining = _parser(tokens_to_match)
            except TypeError:
                consumed, remaining = _parser()(tokens_to_match)
            if not consumed is None:
                return consumed, remaining
        return None, tokens_to_match
    return parser


def and_combinator(parsers):
    def parser(tokens_to_match):
        remaining = tokens_to_match
        rule_consumed = []
        for _parser in parsers:
            try:
                consumed, remaining = _parser(remaining)
            except TypeError:
                consumed, remaining = _parser()(remaining)
            if consumed is None:
                return None, tokens_to_match
            rule_consumed += consumed
        return rule_consumed, remaining
    return parser


AND = and_combinator
OR = or_combinator

S = lambda: OR([S1, A])
S1 = lambda: AND([L_PAREN, S2])
S2 = lambda: OR([AND([R_PAREN, S3]), AND([E, R_PAREN, S3])])
S3 = lambda: OR([S1, EPSILON])
E = lambda: OR([AND([E1, S]), AND([E2, S, S]), AND([B1, S]), AND([B2, S, S])])

A = ATOM
S = S()
S1 = S1()
S2 = S2()
S3 = S3()
E = E()

is_operator = lambda tok: tok.type.startswith("O")
is_value = lambda tok: tok.type.startswith("V")
is_paren = lambda tok: tok.type in ['L_PAREN', 'R_PAREN']

def generate_code(tokens):
    return " ".join(
        reversed([tok.gforth_value for tok in tokens if not is_paren(tok)]))
