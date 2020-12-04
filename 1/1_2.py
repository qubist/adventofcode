import numpy as np
from math import prod

puzzleInput = [1772, 1065, 1827, 1671, 1181, 1915, 1657, 1632, 1053, 1546, 1039, 1388, 1698, 1174, 1275, 1250, 1988, 1078, 1075, 1958, 1617, 1387, 1543, 1965, 1867, 1771, 1755, 1331, 1677, 1935, 1488, 911, 1001, 1516, 1949, 1626, 1083, 1402, 1223, 1179, 2001, 1790, 1551, 1117, 1990, 1968, 1532, 1999, 1175, 1126, 1869, 1666, 1753, 513, 1349, 1139, 1941, 1823, 1647, 1835, 1943, 1459, 1833, 1398, 1877, 1625, 1749, 1631, 1864, 1826, 1499, 1336, 1264, 1091, 1558, 1321, 1754, 1729, 1585, 1740, 1767, 1774, 1164, 1318, 1930, 1236, 1995, 1611, 1319, 1361, 1119, 1563, 1578, 1047, 1797, 1787, 1038, 1921, 1656, 1898, 1828, 1727, 1825, 2010, 536, 1395, 1865, 1882, 1638, 1954, 1565, 1296, 1723, 1187, 60, 1130, 1102, 1963, 1048, 1493, 1795, 472, 1496, 1278, 1444, 1889, 860, 1975, 1961, 1070, 1570, 1495, 1644, 1881, 1293, 1090, 1906, 1385, 1549, 1143, 1195, 2004, 1397, 1032, 1681, 2000, 1574, 1400, 1911, 1868, 1917, 1872, 1696, 1086, 1291, 1761, 1703, 1202, 1486, 1705, 1924, 1186, 1676, 1615, 1951, 1556, 1604, 1534, 2002, 1334, 1109, 1108, 1713, 1422, 1909, 1418, 1592, 1887, 1037, 1568, 1914, 1780, 1929, 1973, 1684, 1581, 1148, 1931, 1619, 1082, 1166, 1913, 1312, 1330, 1540, 1841, 1977, 1769, 1691, 1821]

# toy input
toyPuzzleInput = [1721, 979, 366, 299, 675, 1456]

class TwoDSumsGrid():
    def __init__(self, input):
        self.values = input
        self.dimension = len(self.values)

        grid = [[value] * self.dimension for value in self.values]

        for y in range(self.dimension):
            for x in range(self.dimension):
                # print(f"adding in row {y}, column {x}")
                grid[y][x] += self.values[x]
        self.grid = grid

    def __str__(self):
        out = ""
        y = -1
        for line in [range(self.dimension)] + self.grid:
            out += str(y) if y != -1 else ''
            out += '\t'
            for item in line:
                out += str(item) + '\t'
            out += '\n'
            y += 1
        return out

    # returns list of locations number appears in grid
    # assumes no duplicates
    def find(self, num):
        locs = []
        for i, row in enumerate(self.grid):
            try:
                x = row.index(num)
            except:
                continue
            y = i
            locs.append((x, y))
        return locs

    def lookup(self, x, y):
        return self.grid[y][x]

    # returns the original numbers that made the sum in the specified location
    def origins(self, x, y):
        return (self.values[x], self.values[y])

    def product(self, x, y):
        return self.origins(x, y)[0] * self.origins(x, y)[1]

    def find2020s(self):
        return self.find(2020)

    def productOf2020s(self):
        tts = self.find(2020)
        tt = tts[0]
        return self.product(tt[0], tt[1])

# toyPuzzleGrid = TwoDSumsGrid(toyPuzzleInput)
#
# print(toyPuzzleGrid)
#
# twentytwenties = toyPuzzleGrid.find(2020)
# print(twentytwenties)
# print(toyPuzzleGrid.lookup(twentytwenties[0][0], twentytwenties[0][1]))
# print(toyPuzzleGrid.origins(twentytwenties[0][0], twentytwenties[0][1]))
# print(toyPuzzleGrid.product(twentytwenties[0][0], twentytwenties[0][1]))
#
# puzzleGrid = TwoDSumsGrid(puzzleInput)
# print(puzzleGrid.find2020s())
# print(puzzleGrid.productOf2020s())

class ThreeDSumsGrid():
    def __init__(self, input):
        self.values = input
        self.dimension = len(self.values)

        twoDgrid = TwoDSumsGrid(input).grid

        # doesn't work
        grid = [[[value] * self.dimension for value in self.values] for value in self.values]
        print(grid)
        for y in range(self.dimension):
            # each row is increased by its coord-related amount
            print("item at y:")
            print(grid[y])
            print([[item + self.values[yCoord] for item in list] for yCoord, list in enumerate(grid[y])])
            grid[y] = [[item + self.values[y] for y, item in enumerate(list)] for yCoord, list in enumerate(grid[y])]
            print("item at y NOW:")
            print(grid[y])
            for x in range(self.dimension):
                # Each z-stack gets increased by its coord-related amount
                grid[y][x] = [i + self.values[p] for p, i in enumerate(grid[y][x])]
        self.grid = grid

    def __str__(self):
        out = ""
        y = -1
        for line in [range(self.dimension)] + self.grid:
            out += str(y) if y != -1 else ''
            out += '\t'
            for item in line:
                out += str(item) + '\t'
            out += '\n'
            y += 1
        return out

    # returns list of locations number appears in grid
    # assumes no duplicates
    def find(self, num):
        locs = []
        for i, row in enumerate(self.grid):
            try:
                x = row.index(num)
            except:
                continue
            y = i
            locs.append((x, y))
        return locs

    def lookup(self, x, y):
        return self.grid[y][x]

    # returns the original numbers that made the sum in the specified location
    def origins(self, x, y):
        return (self.values[x], self.values[y])

    def product(self, x, y):
        return self.origins(x, y)[0] * self.origins(x, y)[1]

    def find2020s(self):
        return self.find(2020)

    def productOf2020s(self):
        tts = self.find(2020)
        tt = tts[0]
        return self.product(tt[0], tt[1])

# toyPuzzleGrid3 = ThreeDSumsGrid(toyPuzzleInput)
#
# print("grid with str")
# print(toyPuzzleGrid3)
# print("real grid")
# print(toyPuzzleGrid3.grid)
#
# twentytwenties3 = toyPuzzleGrid3.find(2020)
# print(twentytwenties3)
# print(toyPuzzleGrid3.lookup(twentytwenties3[0][0], twentytwenties3[0][1]))
# print(toyPuzzleGrid3.origins(twentytwenties3[0][0], twentytwenties3[0][1]))
# print(toyPuzzleGrid3.product(twentytwenties3[0][0], twentytwenties3[0][1]))


class NDSumsGrid():
    def __init__(self, input, n):
        self.values = input
        self.sideLength = len(self.values)
        self.n = n
        self.dimensions = (self.sideLength,) * n # (6,6) for toy with n=2
        print(f"dimensions: {self.dimensions}")

        blankMatrix = np.ndarray(shape=self.dimensions, dtype=int, buffer=np.zeros(self.dimensions))
        print(blankMatrix)

        # define an adder array, values filled along one axis
        # starts with x axis
        repeatEach = self.sideLength**(n-1)
        b = np.repeat(input, repeatEach)
        adder = np.ndarray(shape=self.dimensions, dtype=int, buffer=b)
        print("adder:")
        print(adder)

        # not generalized
        if n == 2:
            for axesOrder in [(0,1),(1,0)]:
                blankMatrix += np.transpose(adder, axesOrder)
        elif n == 3:
            for axesOrder in [(0,1,2),(2,0,1),(1,2,0)]:
                blankMatrix += np.transpose(adder, axesOrder)

        self.grid = blankMatrix

    def __str__(self):
        return f"{self.n}-dimensional Sums grid: \n{self.grid}"

    # returns list of locations number appears in grid
    def find(self, num):
        return np.where(self.grid == num)

    def lookup(self, loc):
        return self.grid[loc]

    # returns the original numbers that made the sum in the specified location
    # should take n-long array-like
    def origins(self, loc):
        # print(f'len(loc): {len(loc)}')
        # print(f'self.n: {self.n}')
        assert len(loc) == self.n
        return [self.values[x] for x in loc]

    def product(self, loc):
        return prod(self.origins(loc))

    def find2020s(self):
        return self.find(2020)

    def productOf2020s(self):
        tts = self.find(2020)
        print(f'tts: {tts}')
        tt = np.unique(tts[0])
        print(f'tt: {tt}')
        return self.product(tt)

toyPuzzleGrid_2D = NDSumsGrid(toyPuzzleInput, 2)

print(toyPuzzleGrid_2D)
print(toyPuzzleGrid_2D.find(2020))
print(toyPuzzleGrid_2D.productOf2020s())

toyPuzzleGrid_3D = NDSumsGrid(toyPuzzleInput, 3)

print(toyPuzzleGrid_3D)
print(toyPuzzleGrid_3D.find(2020))
print(toyPuzzleGrid_3D.productOf2020s())

puzzleGrid_3D = NDSumsGrid(puzzleInput, 3)
print(puzzleGrid_3D.productOf2020s())
