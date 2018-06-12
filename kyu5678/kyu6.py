

def queue_time(customers, n):
    if n == 0:
        return "invalid n!"

    queues = [[] for i in range(n)]
    for c in customers:
        queues[shortest_queue_index(queues)].append(c)
    return max(sum(q) for q in queues)


def shortest_queue_index(queues):
    minSum = sum(queues[0])
    index = 0
    for q in range(0, len(queues)):
        if sum(queues[q]) < minSum:
            minSum = sum(queues[q])
            index = q
    return index

#CH6: IQ Test

def iq_test(numbers):
    numbers = numbers.split(' ')
    numbers = [int(i) for i in numbers]
    odd, even = -1, -1
    flagOdd = False
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            if even != -1:
                flagOdd = True
            even = i + 1
        else:
            odd = i + 1
    if flagOdd:
        return odd
    else:
        return even



#CH6: Tribonacci Sequence
def tribonacci(signature, n):
    seq = []
    for i in range(min(n, 3)):
        seq.append(signature[i])
    for i in range(3,n):
        seq.append(seq[i-1] + seq[i-2] + seq[i-3])
    return seq


#CH6: Counting Duplicates
# sooooooo many possible solutions o.o
def duplicate_count(text):
    dicto = {}
    copies = 0
    for i in text.lower():
        if i in dicto:
            dicto[i] += 1
        else:
            dicto[i] = 1
    for j in dicto:
        if dicto[j] > 1:
            copies += 1
    return copies


#CH6: Unique In Order
def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    result = [iterable[0]]
    for i in range(1, len(iterable)):
        if iterable[i] != result[-1]:
            result.append(iterable[i])
    return result


#CH6: Stop gninnipS My sdroW!
def spin_words(sentence):
    words = sentence.split(' ')
    new_words = []
    for word in words:
        if len(word)> 4:
            new_words.append(word[::-1])
        else:
            new_words.append(word)
    return (' ').join(new_words)

#CH6: Find the missing letter
def find_missing_letter(chars):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    offset = alpha.find(chars[0].lower())
    for i in range(len(chars)):
        if not chars[i].lower() == alpha[i + offset]:
            return alpha[i + offset] if chars[0].islower() else alpha[i + offset].upper()

#CH6: Vector Operations and Functionals
def vector_op(func, *vs):
    # for just the first element: func([element[0] for element in vs])
    return [func([element[index] for element in vs]) for index in range(len(vs[0]))]


def iter_mult(xs):
    res = 1
    for ele in xs:
        res *= ele
    return res


def iter_eq(xs):
    if len(xs) == 1: return xs[0]
    value = xs[0]
    for ele in xs:
        if ele != value:
            return False
    return True


#CH6: Build a pile of Cubes
def find_nb(m):
    root = int(m**(1/4) * 1.4)
    naeherung = calculate_nb(root)
    while not naeherung > m:
        if naeherung == m:
            return root
        root += 1
        naeherung = calculate_nb(root)
    return -1
    # print("m: {0} root: {1} nb(root): {2} nb(root+1): {3}".format(m, root, calculate_nb(root), calculate_nb(root+1)))


#somehow it gives a wrong value
def calculate_nb(n):
    return int((n**4 + 2*n**3 + n**2)/4)

def check_calc_nb(n):
    summeSimple = 0
    for i in range(n+1):
        summeSimple += i**3
    summeCalc = calculate_nb(n)
    print ("simple: {} calc: {}".format(summeSimple, summeCalc))
    if summeCalc != summeSimple:
        print("diff is %d" % (summeSimple - summeCalc))
    return summeSimple == summeCalc

#CH6: Street Fighter 2 - Character Selection
def street_fighter_selection(fighters, initial_position, moves):
    selected = []
    pos = [i for i in initial_position]
    for move in moves:
        pos = do_move(pos, move, fighters)
        selected.append(fighters[pos[1]][pos[0]])
    return selected

def do_move(pos, move, array):
    x, y = len(array[0]), len(array) -1
    if move == 'right':
        pos[0] = (pos[0] + 1) % x
    elif move == 'left':
        pos[0] = (pos[0] - 1) % x
    elif move == 'up':
        pos[1] = max(0, pos[1] - 1)
    elif move == 'down':
        pos[1] = min(y, pos[1] + 1)
    return pos

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
start_pos = (0,0)

#CH6: Decode the Morse code
#in code_wars MORSE_CODE is preloaded
MORSE_CODE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B', '-..-': 'X',
              '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S',
              '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O',
              '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7',
              '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q',
              '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@',
              '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}

def decodeMorse(morse_code):
    words = morse_code.strip().split('   ')
    readables = []
    for word in words:
        t, letter = '', word.split(' ')
        for l in letter:
            t += MORSE_CODE[l]
        readables.append(t)
    return ' '.join(readables)