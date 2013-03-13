class Token(object):

    def __init__(self, value, type, gforth_value):
        self.value = value if type != 'V_INT' else "{0}.0".format(value)
        self.type = type
        self.gforth_value = gforth_value or self.value

    def __repr__(self):
        return "<%s>"%(self.gforth_value)

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.value == other.value and self.type == other.type


real_re = ("^\d+\.\d+$", 'V_REAL', '') #  MUST GO BEFORE INT_RE
int_re = ("^\d+$", 'V_INT', '')
bool_re = ("^(true|false)$", 'V_BOOL', '')
e_re = ("^e$", 'V_E', ' 2.718281828459045')
atom_re = (r"^.*$", 'V_STRING', '') #  MUST GO LAST !!!!!
l_paren_re = ('^\($', 'L_PAREN', '')
r_paren_re = ('^\)$', 'R_PAREN', '')
sin_re = ("^sin$", 'OF_SIN', 'fsin')
cos_re = ("^cos$", 'OF_COS', 'fcos')
tan_re = ("^tan$", 'OF_TAN', 'ftan')
add_re = ("^\+$", 'OF_ADD', 'f+')
sub_re = ("^\-$", 'OF_SUB', 'f-')
div_re = ("^/$", 'OF_DIV', 'f/')
mul_re = ("^\*$", 'OF_MUL', 'f*')
lt_re = ("^<$", 'OF_LT', 'f<')
gt_re = ("^>$", 'OF_GT', 'f>')
mod_re = ("^\%$", 'OF_MOD', '')
pow_re = ("^\pow$", 'OF_POW', 'f**')
eq_re = ("^=$", 'OF_EQ', 'f=')
and_re = ("^and$", 'OB_AND', '')
or_re = ("^or$", 'OB_OR', '')
not_re = ("^not$", 'OB_NOT', 'invert')
iff_re = ("^iff$", 'OB_IFF', 'xor invert')
neg_re = ("^neg", "OF_NEG", 'fnegate')
exp_re = ("^exp$", "OF_EXP", 'fexp')

parse_order = [real_re, int_re, bool_re, r_paren_re, l_paren_re, sin_re,
               cos_re, tan_re, add_re, sub_re, div_re, mul_re, lt_re, gt_re,
               mod_re, pow_re, eq_re, and_re, or_re, not_re, iff_re, neg_re,
               atom_re]
