#CH7: List Filtering
def filter_list(lis):
    res = []
    for i in lis:
        if type(i) == int:
            res.append(i)
    return res


#CH7: Exes and Ohs
def xo1(string):
    xs, os = 0, 0
    for ltr in string.lower():
        if ltr == 'o':
            os += 1
        elif ltr == 'x':
            xs += 1
    return xs == os

#CH7: Highest and Lowest
def high_and_low(numbers):
    numb = [ int(x) for x in numbers.split(' ')]
    return format('%d %d' % (max(numb), min(numb)))




#CH7: String Reordering
def sentence(liste):
    book = {}
    ordered_words = []
    for dic in liste:
        book.update(dic)
    for i in range (-999, 999):
        if str(i) in book:
            ordered_words.append(book[str(i)])
    return ' '.join(ordered_words)

