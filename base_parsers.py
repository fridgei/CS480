from tokens import Token

_UNARY_NUM_OPS = [Token('', 'O_COS'), Token('', 'O_SIN'), Token('', 'O_TAN'),
                  Token('', 'O_NEG'), Token('', 'O_EXP'), Token('', 'O_LOGN')]
_BINARY_NUM_OPS = [Token('', 'O_ADD'), Token('', 'O_SUB'), Token('', 'O_DIV'),
                   Token('', 'O_MUL'), Token('', 'O_LT'), Token('', 'O_GT'),
                   Token('', 'O_EQ'), Token('', 'O_POW'), Token('', 'O_MOD')]
_UNARY_BOOL_OPS = [Token('', 'O_NOT')]
_BINARY_BOOL_OPS = [Token('', 'O_AND'), Token('', 'O_OR')]
_BOOL = [Token('', 'V_BOOL')]
_NUM = [Token('', 'V_INT'), Token('', 'V_REAL'), Token('', 'V_E')]
_LPAREN = [Token('', 'L_PAREN')]
_RPAREN = [Token('', 'R_PAREN')]


def EPSILON(tokens):
    print "EPSILON CAN DO IT"
    print tokens
    return [], tokens


def match_tokens(possible_matchs):
    def parser(tokens):
        if not tokens:
            return None, []
        for match in possible_matchs:
            if tokens[0].type == match.type:
                print "{0} is {1}".format(tokens[0].type, match.type)
                return [tokens[0]], tokens[1:]
            else:
                print "{0} is not {1}".format(tokens[0].type, match.type)
        return None, tokens
    return parser


L_PAREN = match_tokens(_LPAREN)
R_PAREN = match_tokens(_RPAREN)
E1 = match_tokens(_UNARY_NUM_OPS)
E2 = match_tokens(_BINARY_NUM_OPS)
B1 = match_tokens(_UNARY_BOOL_OPS)
B2 = match_tokens(_BINARY_BOOL_OPS)
BOOL = match_tokens(_BOOL)
NUM = match_tokens(_NUM)
