import sys
from tokenizer import tokenize
from combinator import S, S1, S2, E

get_str = lambda x: " ".join(map(lambda y: y.value, x))
for arg in sys.argv[1:]:
    with open(arg) as f:
        tokens = tokenize(f.read())
        print "Testing:\n {0}".format(get_str(tokens))
        consumed, remaining = S(tokens)
        if remaining:
            if consumed is not None:
                print get_str(tokens)
                print "Error at"
                print "{0} -> {1}\n".format(get_str(consumed),
                                            get_str(remaining))
            else:
                print "Rejected"
                print get_str(tokens)
        else:
            print "Accepted"
            print get_str(consumed)
            print generate_code(consumed)
