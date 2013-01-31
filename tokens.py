#  primitives
real_re = (r"\d+.\d+\B", 'V_REAL') #  MUST GO BEFORE INT_RE
int_re = ("\b\d+\b", 'V_INT')
bool_re = (r"(\btrue\b|\bfalse\b)", 'V_BOOL')
e_re = ("\be\b", 'V_E')
atom_re = (r"\b.*\b", 'V_STRING') #  MUST GO LAST !!!!!
#  primitive type declarations
bool_type_re = (r"\bbool\b", 'T_BOOL')
real_type_re = (r"\breal\b", 'T_REAL')
int_type_re = (r"\bint\b", 'T_INT')
string_type_re = (r"\bstring\b", 'T_STRING')
#  expressions
print_re = (r"\bprintln\b", 'E_PRINT')
assign_re = (r"\bassign\b", 'E_ASSIGN')
let_re = (r"\blet\b", 'E_LET')
if_re = (r"\bif\b", 'E_IF')
while_re = (r"\bwhile\b", 'E_WHILE')
l_paren_re = ('\(', 'L_PAREN')
r_paren_re = ('\)', 'R_PAREN')
#  operators
logn_re = (r"\blogn\b", 'O_LOGN')
sin_re = (r"\bsin\b", 'O_SIN')
cos_re = (r"\bcos\b", 'O_COS')
tan_re = (r"\btan\b", 'O_TAN')
add_re = ("\+", 'O_ADD')
sub_re = ("\-", 'O_SUB')
div_re = (r"\\", 'O_DIV')
mul_re = ("\*", 'O_MUL')
lt_re = (r"<", 'O_LT')
gt_re = (r">", 'O_GT')
mod_re = (r"\%", 'O_MOD')
pow_re = (r"\^", 'O_POW')
eq_re = (r"=", 'O_EQ')
parse_order = [real_re, int_re, bool_re, r_paren_re, l_paren_re, bool_type_re,
               real_type_re, int_type_re, string_type_re, print_re, assign_re,
               let_re, if_re, while_re, logn_re, sin_re, cos_re, tan_re,
               add_re, sub_re, div_re, mul_re, lt_re, gt_re, mod_re, pow_re,
               eq_re, atom_re]


class Token(object):

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return "<%s, %s>"%(self.type, self.value)
