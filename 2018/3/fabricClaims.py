fabricSize = 1000

# Fabric of size size. It's a matrix of numbers represending how many claims
# mention that square inch. Also takes a ClaimList object as input.
class Fabric():
    def __init__(self, size):
        self.size = size

        self.matrix = [[0] * self.size for _ in range(self.size)]

    def findUnoverlappingClaim(self, claimsList):
        for claim in claimsList.list:
            if not self.claimHasOverlap(claim):
                return claim.ID

    def claimHasOverlap(self, claim):
        # iterate through claim area and return True if we find anything
        # bigger than 1
        startingPoint = (claim.left, claim.top)
        endingPoint = (claim.left+claim.x, claim.top+claim.y)
        x = startingPoint[0]
        y = startingPoint[1]
        while y < endingPoint[1]:
            while x < endingPoint[0]:
                if self.matrix[y][x] > 1:
                    return True
                x += 1
            x = startingPoint[0]
            y += 1
        return False

    def countOverlaps(self):
        count = 0
        y = 0
        x = 0
        while y < self.size:
            while x < self.size:
                if self.matrix[y][x] > 1:
                    count += 1
                x += 1
            x = 0
            y += 1
        return count

    def applyClaim(self, claim):
        startingPoint = (claim.left, claim.top)
        endingPoint = (claim.left+claim.x, claim.top+claim.y)
        x = startingPoint[0]
        y = startingPoint[1]
        while y < endingPoint[1]:
            while x < endingPoint[0]:
                self.matrix[y][x] += 1
                x += 1
            x = startingPoint[0]
            y += 1

    def applyClaims(self, claimsList):
        for claim in claimsList.list:
            self.applyClaim(claim)

    def __str__(self):
        out = ''
        for x in self.matrix:
            i = 0
            while i < len(x):
                out += str(x[i])
                i += 1
            out += "\n"
        return out

class ClaimList():
    def __init__(self, file):
        self.fileName = file
        self.list = []

    def loadClaims(self):
        with open(self.fileName) as input:
            claims = input.read().splitlines()
            for claim in claims:
                # find ID
                readID = ''
                i = 0
                while i < len(claim):
                    letter = claim[i]
                    if letter == ' ':
                        break
                    readID += letter
                    i += 1
                id = readID[1:]
                # find leftBuffer
                readLeft = ''
                while i < len(claim):
                    letter = claim[i]
                    if letter == ',':
                        break
                    readLeft += letter
                    i += 1
                left = readLeft[3:]
                # find topBuffer
                readTop = ''
                while i < len(claim):
                    letter = claim[i]
                    if letter == ':':
                        break
                    readTop += letter
                    i += 1
                top = readTop[1:]
                # find x
                readX = ''
                while i < len(claim):
                    letter = claim[i]
                    if letter == 'x':
                        break
                    readX += letter
                    i += 1
                x = readX[2:]
                # find y
                readY = ''
                while i < len(claim):
                    letter = claim[i]
                    if letter == ':':
                        break
                    readY += letter
                    i += 1
                y = readY[1:]
                self.list.append(Claim(int(id), int(left), int(top), int(x), int(y)))

    def getClaimByID(self, ID):
        for claim in self.list:
            if claim.ID == ID:
                return claim
        raise Exception(f"Couldn't find claim with ID `{ID}`")

    def __str__(self):
        output = []
        for claim in self.list:
            output.append(f"{claim}")
        return str(output) # fixme?

class Claim():
    def __init__(self, ID, leftBuffer, topBuffer, x, y):
        self.ID = ID
        self.left = leftBuffer
        self.top = topBuffer
        self.x = x
        self.y = y

        self.size = (leftBuffer + x, topBuffer + y)

    def __str__(self):
        return f"#{self.ID} @ {self.left},{self.top}: {self.x}x{self.y} ({self.size[0]}x{self.size[1]})"

c = Claim(123, 3, 2, 5, 4)

# print(c)

l = ClaimList("input.txt")
l.loadClaims()
# print(l)

f = Fabric(fabricSize)

# print(f)
f.applyClaims(l)
print(f)

print(f.countOverlaps())

print(f.claimHasOverlap(l.list[2]))
print(f.findUnoverlappingClaim(l))
