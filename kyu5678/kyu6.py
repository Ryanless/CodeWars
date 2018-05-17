

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
