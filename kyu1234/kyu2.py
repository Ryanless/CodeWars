import itertools

#CH2: 6 By 6 Skyscrapers
def solve_puzzle(clues):
    p0 = get_possible_perm(0)
    p1 = get_possible_perm(1)
    p2 = get_possible_perm(2)
    p3 = get_possible_perm(3)
    p4 = get_possible_perm(4)
    p5 = get_possible_perm(5)
    p6 = get_possible_perm(6)


    return None


def get_visible(line):
    count = 1
    highest = line[0]
    for i in range(1, len(line)):
        if line[i] > highest:
            count += 1
            highest = line[i]
    return count


def get_possible_perm(visCount):
    all = list(itertools.permutations([1, 2, 3, 4, 5, 6]))
    posib = get_perm_list(all, visCount)
    #print('for Nr {} the count is {}'.format(visCount, len(posib)))
    return posib


def get_2_cues_perm(arrA, countB):
    copyA = []
    for perm in arrA: copyA.append(perm[::-1])
    posib = get_perm_list(copyA, countB)
    #print('for Nr {} the sub count is {}'.format(countB, len(posib)))
    return posib


def get_perm_list(perm_array, visCount):
    if visCount == 0: return perm_array
    posib = []
    for perm in perm_array:
        if get_visible(perm) == visCount: posib.append(perm)
    return posib



class SkyscraperField:

    perm_rows = []
    perm_columns = []
    used_rows = [[] for aa in range(6)]
    used_columns = [[] for bb in range(6)]
    _field = [[0] * 6 for ii in range(6)]
    possibilityField = [[[*range(1, 7)] for jj in range(6)] for kk in range(6)]

    def __init__(self, clues):
        self.clues = clues
        self.possiblePerms = []
        self.height = len(self._field)
        self.width = len(self._field[0])
        for i in range(7):
            p = get_possible_perm(i)
            self.possiblePerms.append(p)
        self.setupLines()

    def recalculatePossibilityField(self):
        for y in range(self.height):
            rowPos = 0
            for x in range(self.width):
                r = self.calculateCellPosibilities(y, x)
                self.possibilityField[y][x] = r
                if len(r) == 1:
                    # print('Bingo! x:{} y:{} is {}'.format(x, y, r[0]))
                    self.setCell(y, x, r[0])
                rowPos += len(r)
            # print('Row {} has {} total posibilities'.format(y, rowPos))


    def setCell(self, y, x, value):
        self._field[y][x] = value
        self.used_columns[x].append(value)
        self.used_rows[y].append(value)



    #Uses the rows & columns to find/eliminate possibilities of the target cell
    def calculateCellPosibilities(self, y, x):
        p_row = (z[x] for z in self.perm_rows[y])
        p_col = (z[y] for z in self.perm_columns[x])
        inter = set(p_row).intersection(p_col)
        old = self.possibilityField[y][x]
        inter = set(inter).intersection(old)
        return list(inter)


    def setupLines(self):
        for x in range(6):
            nrX = self.clues[17 - x]
            column = get_2_cues_perm(self.possiblePerms[nrX], self.clues[x])
            self.perm_columns.append(column)

        for y in range(23, 17, -1):
            nrY = self.clues[29 - y]
            row = get_2_cues_perm(self.possiblePerms[nrY], self.clues[y])
            self.perm_rows.append(row)


    def filterLines(self):
        #filter the lines in which you have values
        for y in range(self.height):
            for x in range(self.width):
                value = self._field[y][x]
                if value != 0:
                    self.perm_columns[x] = [col for col in self.perm_columns[x] if col[y] == value]
                    self.perm_rows[y] = [row for row in self.perm_rows[y] if row[x] == value]

        #filter the lines which are restricted to have already used values
        for y in range(self.height):
            if self.used_rows[y] != []:
                for xx in range(self.width):
                    self.perm_columns[xx] = [col for col in self.perm_columns[xx] if col[y] not in self.used_rows[y] or self._field[y][xx] != 0]

        for x in range(self.width):
            if self.used_columns[x] != []:
                for yy in range(self.height):
                    self.perm_rows[yy] = [row for row in self.perm_rows[yy] if row[x] not in self.used_columns[y] or self._field[yy][x] != 0]



    def pretty_print(self):
        border = '    {}   {}   {}   {}   {}   {}\n'
        body = '{} | {} | {} | {} | {} | {} | {} | {}\n'
        wall = ' '*3 + '-'*23 + '\n'
        str1 = border.format(*self.clues[:6])
        str3 = body.format(self.clues[23], *self._field[0], self.clues[6])
        str4 = body.format(self.clues[22], *self._field[1], self.clues[7])
        str5 = body.format(self.clues[21], *self._field[2], self.clues[8])
        str6 = body.format(self.clues[20], *self._field[3], self.clues[9])
        str7 = body.format(self.clues[19], *self._field[4], self.clues[10])
        str8 = body.format(self.clues[18], *self._field[5], self.clues[11])

        str10 = border.format(*self.clues[17:11:-1])

        complete = str1 + wall + str3 + str4 + str5 + str6 + str7 + str8 + wall + str10

        print(complete)


    def print_lines(self):
        for i in range(len(self.perm_rows)):
            print('Row {} has {} possibilities'.format(i + 1, len(self.perm_rows[i])))
        for j in range(len(self.perm_columns)):
            print('Column {} has {} possibilities'.format(j + 1, len(self.perm_columns[j])))

