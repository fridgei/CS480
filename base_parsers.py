from tokens import Token


def EPSILON(tokens):
    return [], tokens


def match_tokens(possible_matchs):
    def parser(tokens):
        if not tokens:
            return None, []
        for match in possible_matchs:
            if tokens[0].type == match.type:
                return [tokens[0]], tokens[1:]
        return None, tokens
    return parser


L_PAREN = match_tokens([Token('', 'L_PAREN')])
R_PAREN = match_tokens([Token('', 'R_PAREN')])
E1 = match_tokens([Token('', 'OF_COS'), Token('', 'OF_SIN'),
                  Token('', 'OF_TAN'), Token('', 'OF_NEG'),
                  Token('', 'OF_EXP'), Token('', 'OF_LOGN')])
E2 = match_tokens([Token('', 'OF_ADD'), Token('', 'OF_SUB'), Token('','OF_DIV'),
                   Token('', 'OF_MUL'), Token('', 'OF_LT'), Token('', 'OF_GT'),
                   Token('', 'OF_EQ'), Token('', 'OF_POW'), Token('', 'OF_MOD')])
B1 = match_tokens([Token('', 'OB_NOT')])
B2 = match_tokens([Token('', 'OB_AND'), Token('', 'OB_OR'), Token('', 'OB_IFF')])
ATOM = match_tokens([Token('', 'V_BOOL'), Token('', 'V_INT'), Token('',
                    'V_REAL'), Token('', 'V_E')])
