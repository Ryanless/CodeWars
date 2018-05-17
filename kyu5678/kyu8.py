#CH8: Expressions Matter
def expression_matter1(a, b, c):
    if a == 1 and c == 1:
        return a + b + c
    elif a == 1 and b == 1:
        return (a + b) * c
    elif b == 1 and c == 1:
        return a * (b + c)
    elif a == 1:
        return (a + b) * c
    elif b == 1:
        return (min(a,c) + b)*max(a,c)
    elif c == 1:
        return a * (b + c)
    else:
        return a * b * c


def expression_matter(a, b, c):
    return max(a + b + c, (a + b) * c, a * (b + c), a * b * c)