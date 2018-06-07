import re

#CH: Number of trailing zeros of N!

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

#CH: Letterss of Natac

#times out
def play_if_enough2(hand, play):
    #build dict of the resources you have
    resources = {}
    for charA in hand:
        if charA in resources.keys():
            resources[charA] += 1
        else:
            resources[charA] = 1
    #checks if you have enough resources to build play
    for charB in play:
        if (charB in resources) and (resources[charB] > 0):
            resources[charB] -= 1
        else:
            return False, hand
    #compute your new hand after spending resources
    newHand = ''
    for key in resources.keys():
        newHand += key * resources[key]
    return True, newHand


#works, but can be simplified
def play_if_enough3(hand, play):
    new_resources = {}
    new_hand = ''
    for char in 'abcdefghijklmnopqrstuvwxyz':
        new_resources[char] = hand.count(char) - play.count(char)
        if new_resources[char] < 0:
            return False, hand
        else:
            new_hand += char * new_resources[char]
    return True, new_hand

def play_if_enough(hand, play):
    new_hand = ''
    for char in 'abcdefghijklmnopqrstuvwxyz':
        new_res = hand.count(char) - play.count(char)
        if new_res < 0:
            return False, hand
        else:
            new_hand += char * new_res
    return True, new_hand

#CH: Typoglycemia Generator
def scramble_words(words):
    word_array = words.split(" ")
    result = []
    for word in word_array:
        scrambled = scramble_word(word)
        result.append(scrambled)
    return ' '.join(result)


def scramble_word(word):
    if len(word) <= 2:
        return word
    else:

        start, end = '', ''
        if word[0] in "-',.":
            start = word[0]
            word = word[1:]
        if word[-1] in "-',.":
            end = word[-1]
            word = word[:-1]

        new_word = word[0]
        shorted_word = word[1: -1]
        for char in 'abcdefghijklmnopqrstuvwxyz':
            new_word += char * shorted_word.count(char)

        for index in range(1, len(word) - 1):
            if word[index] in "-',.":
                new_word = new_word[:index] + word[index] + new_word[index:]

        return start + new_word + word[-1] + end


#CH: Calculate the derivative of a polynomial
def derivative(poly_deriv):
    reSplitter = re.compile( r'[\+-]?[^\+-]+')
    simple_deriv = reSplitter.findall(poly_deriv)
    result = ''
    for i in simple_deriv:
        result += simple_derivative(i)
    if result == '':
        return '0'
    else:
        return result


def simple_derivative(simple_der):
    reMatcher = re.compile(r'([\+\-])?(\d+)?(x)(\^(\d+))?') # Making the x mandatory makes the derivative of normal numbers
    matched = reMatcher.match(simple_der)
    if matched == None:
        return ''
    # a * x ^ b --> (a * b) * x ^(b - 1)
    sign = matched.group(1)
    if sign == None:
        sign = ''
    a  = matched.group(2)
    if a == None:
        a = 1
    else:
        a = int(a)
    a_new = a
    b = matched.group(5)
    if b != None:
        b = int(b)
    elif matched.group(3) != None:
        b = 1
    else:
        b = 0
    a_new = a * b
    b_new = b - 1
    result = ''
    if a == 0:
        print
        return result
    elif a_new == 1:
        if b_new == 0:
            result += sign + '1'
        else:
            result += sign
    else:
        result += sign + str(a_new)
    if b_new == 1:
        result += "x"
    elif b_new != 0:
        result += "x^" + str(b_new)
    return result



#CH: Car Park Escape
def escape(carpark):
    solution = []
    currPos = None
    _flagBreak = False
    for lv in carpark:
        if _flagBreak: break
        for i in lv:
            if i == 2:
                currPos = [lv.index(i), carpark.index(lv)]
                _flagBreak = True
                break

    while currPos[1] != len(carpark) -1:
        floor = carpark[currPos[1]]
        for j in range(len(floor)):
            if floor[j] == 1:
                diff = j - currPos[0]
                getSolutionString(diff, solution)
                currPos[1] += 1
                currPos[0] = j
                break
    diff = len(carpark[currPos[1]]) - 1 - currPos[0]
    getSolutionString(diff, solution, True)

    return solution


def getSolutionString(diff, solution, isLast = False):
    if diff == 0:
        if len(solution) == 0 or isLast: return
        solution[-1] = 'D' + str(int(solution[-1][1:]) + 1)
    elif diff > 0:
        solution.append('R' + str(diff))
        if not isLast: solution.append('D1')
    else:
        solution.append('L' + str(abs(diff)))
        if not isLast: solution.append('D1')


#CH5: Weight for weight
def order_weight_try1(string):
    #this version fails to sort the numbers that have the same quersumme
    weights = [ [int(x), sum([int(i) for i in x]) ] for x in string.split(' ')]
    sorted_weights = sorted(weights, key=lambda f: f[1])
    return sorted_weights
    solution = [str(j[0]) for j in sorted_weights]
    return ' '.join(solution)


def order_weight_try2(string):
    weights = {quersumme(j): j for j in string.split(' ')}
    return weights


def order_weight(string):
    if string == "":
        return ""
    weights = [[int(x), quersumme(x)] for x in string.split(' ')]
    quer = sorted(list(set([y[1] for y in weights])))
    sol = []

    for z in quer:
        arr = sorted([str(i[0]) for i in weights if i[1] == z])
        sol.append( ' '.join(arr))
    return ' '.join(sol)


def quersumme(n):
    return sum([int(i) for i in n])


#CH5: Directions Reduction
def dirReduc(arr):
    newArr = arr
    for index in range(1, len(arr)):
        if isOpposite(arr[index], arr[index -1]):
            newArr = dirReduc(arr[:index -1] + arr[index + 1:])
    return newArr

def isOpposite(A, B):
    a, b = A.lower(), B.lower()
    res = -1
    if a == "north":
        res = True if b == "south" else False
    elif a == "south":
        res = True if b == "north" else False
    elif a == "east":
        res = True if b == "west" else False
    elif a == "west":
        res = True if b == "east" else False
    else:
        raise Exception
    return res
