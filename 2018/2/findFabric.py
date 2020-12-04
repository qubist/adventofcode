class Box():
    def __init__(self, ID):
        self.ID = ID

    def __str__(self):
        return self.ID

    # compare two boxes and return the number of letters their IDs differ by
    def compare(self, other):
        # make sure the lengths of the IDs are the same
        if len(self.ID) != len(other.ID):
            print("Something is wrong")
            return
        # walk through my ID and check it against the other's ID
        i = 0
        numDiffs = 0
        while i < len(self.ID):
            if self.ID[i] != other.ID[i]:
                numDiffs += 1
            i += 1
        return numDiffs

class BoxList():
    def __init__(self, file):
        self.fileName = file
        self.list = []

    def loadBoxes(self):
        with open(self.fileName) as input:
            boxIDs = input.read().splitlines()
            for ID in boxIDs:
                self.list.append(Box(ID))

    def getNth(self, n):
        return self.list[n]

    # returns tuple of the IDs of the boxes which have IDs one character apart
    def getCorrectBoxes(self):
        out = []
        for box in self.list:
            for otherBox in self.list:
                if box.compare(otherBox) == 1:
                    return (box.ID, otherBox.ID)

    def solve(self):
        out = ''
        box1 = self.getCorrectBoxes()[0]
        box2 = self.getCorrectBoxes()[1]

        i = 0
        while i < len(box1):
            if box1[i] == box2[i]:
                out += box1[i]
            i += 1
        return out

    # to print a BoxList, print the list of the IDs of the boxes it contains
    def __str__(self):
        output = []
        for box in self.list:
            output.append(f"{box.ID}")
        return f"{output}"

l = BoxList("input.txt")
l.loadBoxes()

print('\nlist of boxes:')
print(l)

print("\nshould be 1:")
print(
    l.getNth(1).compare(l.getNth(4))
    )

print("\ncorrect boxes tuple:")
print(l.getCorrectBoxes())

print(l.solve())
