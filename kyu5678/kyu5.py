

# Number of trailing zeros of N!

# Not efficent enough to pass
def zeros_1(n):
    nrOf5 = 0
    for i in range(2, n+1):
        while i % 5 == 0:
            nrOf5 += 1
            i /= 5
    return nrOf5


def zeros(n):
    c5 = 0
    m = 1
    while n >= m:
        m *= 5
        c5 += n//m
    return c5




