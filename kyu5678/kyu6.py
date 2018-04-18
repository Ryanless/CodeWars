

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
    return  index






a = queue_time([3,4,5,6,7], 2)
print(a)