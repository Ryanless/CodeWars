

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




