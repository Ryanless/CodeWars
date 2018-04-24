
from kyu5678.kyu5 import *

def pseudo_test_func(func, args):
    resultat = func(args)
    print("The input %s has the following result: %s" %(args, resultat))
    return resultat


pseudo_test_func(domain_name, "http://github.com/carbonfive/raygun")
pseudo_test_func(domain_name, "http://www.zombie-bites.com")
pseudo_test_func(domain_name, "https://www.cnet.com")
pseudo_test_func(domain_name, "www.xakep.ru")