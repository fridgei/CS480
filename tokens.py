class Token(object):

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return "<%s>"%(self.type)

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.type == other.type


real_re = ("^\d+\.\d+$", 'V_REAL') #  MUST GO BEFORE INT_RE
int_re = ("^\d+$", 'V_INT')
bool_re = ("^(true|false)$", 'V_BOOL')
e_re = ("^e$", 'V_E')
atom_re = (r"^.*$", 'V_STRING') #  MUST GO LAST !!!!!
l_paren_re = ('^\($', 'L_PAREN')
r_paren_re = ('^\)$', 'R_PAREN')
sin_re = ("^sin$", 'OF_SIN')
cos_re = ("^cos$", 'OF_COS')
tan_re = ("^tan$", 'OF_TAN')
add_re = ("^\+$", 'OF_ADD')
sub_re = ("^\-$", 'OF_SUB')
div_re = (r"\\", 'OF_DIV')
mul_re = ("^\*$", 'OF_MUL')
lt_re = ("^<$", 'OF_LT')
gt_re = ("^>$", 'OF_GT')
mod_re = ("^\%$", 'OF_MOD')
pow_re = ("^\pow$", 'OF_POW')
eq_re = ("^=$", 'OF_EQ')
and_re = ("^and$", 'OB_AND')
or_re = ("^or$", 'OB_OR')
not_re = ("^not$", 'OB_NOT')
iff_re = ("^iff$", 'OB_IFF')
neg_re = ("^neg", "OF_NEG")

parse_order = [real_re, int_re, bool_re, r_paren_re, l_paren_re, sin_re,
               cos_re, tan_re, add_re, sub_re, div_re, mul_re, lt_re, gt_re,
               mod_re, pow_re, eq_re, and_re, or_re, not_re, iff_re, neg_re,
               atom_re]
