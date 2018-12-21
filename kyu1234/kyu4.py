

# Pyramid Slide Down
def longest_slide_down(pyramid):
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
    return pyramid[0][0]


#CH4: Snail
def snail(array):
    if array == [[]]: return []
    result = []
    xMax = yMax = len(array)-1
    xMin = yMin = 0
    while xMax > xMin:
        #make 1 round
        for x in range(xMin, xMax):
            result.append(array[yMin][x])
        for y in range(yMin, yMax):
            result.append(array[y][xMax])
        for x in range(xMax, xMin, -1):
            result.append(array[yMax][x])
        for y in range(yMax, yMin, -1):
            result.append(array[y][xMin])
        xMax -= 1
        yMax -= 1
        xMin += 1
        yMin += 1
    l = len(array)
    if l % 2 != 0: result.append(array[int(l /2)][int(l /2)])
    return result





#CH4:Create a funnel
class Node(object):

    def __init__(self, pos, left, right):
        self.pos = pos
        self.left = left
        self.right = right




class Funnel(object):

    def __init__(self):
        self._numbers = []

    def fill(self, *args):
        for n in args:
            if len(self._numbers) < 15: self._numbers.append(n)

    def drip(self):
        if len(self._numbers) == 0: return None
        r = self._numbers[0]
        #TODO: 2. continue with this kata


        return r

    def __str__(self):
        v = [str(l) for l in self._numbers]
        v += (15 - len(v)) * " "
        print(v)
        rep = "\\{} {} {} {} {}/\n \\{} {} {} {}/\n  \\{} {} {}/\n   \\{} {}/\n    \\{}/"\
            .format(v[10], v[11], v[12], v[13], v[14], v[6], v[7], v[8], v[9],
                    v[3], v[4], v[5], v[1], v[2], v[0])
        return rep

    def weight(self, pos):
        size = len(self._numbers)
        if pos >= size: return 0
        elif pos == 1:
            dic = {2: 0, 3: 0,
                   4: 1, 5: 2, 6: 2,
                   7: 3, 8: 4, 9: 5, 10: 5,
                   11: 6, 12: 7, 13: 8, 14: 9, 15: 9}
            return dic[size]
        elif pos == 2:
            dic = {3: 0, 4: 0, 5: 1, 6: 2,
                   7: 2, 8: 3, 9: 4, 10: 5,
                   11: 5, 12: 6, 13: 7, 14: 8, 15: 9}
            return dic[size]

        elif pos == 3:
            dic = {4: 0, 5: 0, 6: 0,
                   7: 1, 8: 2, 9: 2, 10: 2,
                   11: 3, 12: 4, 13: 5, 14: 5, 15: 5}
            return dic[size]
        elif pos == 4:
            dic = {5: 0, 6: 0,
                   7: 0, 8: 1, 9: 2, 10: 2,
                   11: 2, 12: 3, 13: 4, 14: 5, 15: 5}
            return dic[size]
        elif pos == 5:
            dic = {6: 0,
                   7: 0, 8: 0, 9: 1, 10: 2,
                   11: 2, 12: 2, 13: 3, 14: 4, 15: 5}
            return dic[size]



