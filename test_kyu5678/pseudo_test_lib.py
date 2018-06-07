

def pseudo_test_func(func, args):
    resultat = func(args)
    print("The input %s has the following result: %s" %(args, resultat))
    return resultat

def pseudo_test_func(func, *args):
    resultat = func(*args)
    print("The input %s has the following result: %s" %(args, resultat))
    return resultat