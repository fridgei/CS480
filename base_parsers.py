from tokens import Token

ATOMS = [Token('', 'V_REAL'), Token('', 'V_INT'), Token('', 'V_BOOL'),
        Token('', 'V_E'), Token('', 'T_BOOL'), Token('', 'T_REAL'),
        Token('', 'T_INT'), Token('', 'T_STRING'), Token('', 'E_PRINT'),
        Token('', 'E_ASSIGN'), Token('', 'E_LET'), Token('', 'E_IF'),
        Token('', 'E_WHILE'), Token('', 'O_LOGN'), Token('', 'O_SIN'),
        Token('', 'O_COS'), Token('', 'O_TAN'), Token('', 'O_ADD'),
        Token('', 'O_SUB'), Token('', 'O_DIV'), Token('', 'O_MUL'),
        Token('', 'O_LT'), Token('', 'O_GT'), Token('', 'O_MOD'),
        Token('', 'O_POW'), Token('', 'O_EQ'), Token('', 'V_STRING')]

L_PAREN_T = Token('', 'L_PAREN')
R_PAREN_T = Token('', 'R_PAREN')
EPS = Token('', 'EPSILON')


def ATOM(tokens):
    if not tokens:
        return None, []
    for atom in ATOMS:
        if tokens[0].type is atom.type:
            return tokens[0], tokens[1:]
    return None, tokens


def L_PAREN(tokens):
    if not tokens:
        return None, []
    if tokens[0].type is L_PAREN_T.type:
        return tokens[0], tokens[1:]
    return None, tokens


def R_PAREN(tokens):
    if not tokens:
        return None, []
    if tokens[0].type is R_PAREN_T.type:
        return tokens[0], tokens[1:]
    return None, tokens


def EPSILON(tokens):
    return [], tokens
