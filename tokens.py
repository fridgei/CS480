#  primitives
real_re = ("^\d+\.\d+$", 'V_REAL') #  MUST GO BEFORE INT_RE
int_re = ("^\d+$", 'V_INT')
bool_re = ("^(true|false)$", 'V_BOOL')
e_re = ("^e$", 'V_E')
atom_re = (r"^.*$", 'V_STRING') #  MUST GO LAST !!!!!
#  primitive type declarations
bool_type_re = ("^bool$", 'T_BOOL')
real_type_re = ("^real$", 'T_REAL')
int_type_re = ("^int$", 'T_INT')
string_type_re = (r"^string$", 'T_STRING')
#  expressions
print_re = ("^println$", 'E_PRINT')
assign_re = ("^assign$", 'E_ASSIGN')
let_re = ("^let$", 'E_LET')
if_re = ("^if$", 'E_IF')
while_re = ("^while$", 'E_WHILE')
l_paren_re = ('^\($', 'L_PAREN')
r_paren_re = ('^\)$', 'R_PAREN')
#  operators
logn_re = ("^logn$", 'O_LOGN')
sin_re = ("^sin$", 'O_SIN')
cos_re = ("^cos$", 'O_COS')
tan_re = ("^tan$", 'O_TAN')
add_re = ("^\+$", 'O_ADD')
sub_re = ("^\-$", 'O_SUB')
div_re = (r"\\", 'O_DIV')
mul_re = ("^\*$", 'O_MUL')
lt_re = ("^<$", 'O_LT')
gt_re = ("^>$", 'O_GT')
mod_re = ("^\%$", 'O_MOD')
pow_re = ("^\^$", 'O_POW')
eq_re = ("^=$", 'O_EQ')
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

    def __eq__(self, other):
        if type(self) is not type(other):
            raise Exception("Invalid comparison between "
                            "type {0} and {1}".format(type(self), type(other)))
        return self.value == other.value and self.type == other.type
