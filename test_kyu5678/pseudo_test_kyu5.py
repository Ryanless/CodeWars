
from kyu5678.kyu5 import *

def pseudo_test_func(func, args):
    resultat = func(args)
    print("The input %s has the following result: %s" %(args, resultat))
    return resultat


# pseudo_test_func(domain_name, "http://github.com/carbonfive/raygun")
# pseudo_test_func(domain_name, "http://www.zombie-bites.com")
# pseudo_test_func(domain_name, "https://www.cnet.com")
# pseudo_test_func(domain_name, "www.xakep.ru")

# pseudo_test_func(scramble_words, 'professionals')
# pseudo_test_func(scramble_words, 'i')
# pseudo_test_func(scramble_words, '')
# pseudo_test_func(scramble_words, 'me')
# pseudo_test_func(scramble_words, 'you')
# pseudo_test_func(scramble_words, 'card-carrying')
# pseudo_test_func(scramble_words, "shan't")
# pseudo_test_func(scramble_words, '-dcba')
# pseudo_test_func(scramble_words, 'I can!')

carpark1 = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]

carpark2 = [[2, 0, 0, 1, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]

carpark3 = [[0, 2, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]

carpark4 = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

carpark5 = [[0, 0, 0, 0, 2]]

pseudo_test_func(escape, carpark1)
pseudo_test_func(escape, carpark2)
pseudo_test_func(escape, carpark3)
pseudo_test_func(escape, carpark4)
pseudo_test_func(escape, carpark5)
