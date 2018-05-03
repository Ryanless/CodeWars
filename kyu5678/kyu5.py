

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


# Extract the domain name from a URL


#without regex pattern match
def domain_name(url):
    urlParts = url.split('/')
    if len(urlParts) > 1 and urlParts[1] == '':
        result = urlParts[2].split('.')
    else:
        result = urlParts[0].split('.')
    if result[0] == 'www':
        return result[1]
    else:
        return result[0]


def isPP(n):
    for i in range(2, int(n**0.5)+1):
        ex = 2
        while i**ex <= n:
            if i**ex == n:
                return [i, ex]
            ex += 1
    return None






