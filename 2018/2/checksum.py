with open('input.txt') as input:
    boxIDs = input.read().splitlines()

# takes string like abbacd and returns string bdca
def getLetters(letters):
    return "".join(set(letters))

def countInstance(letter, string):
    output = 0
    for let in string:
        if let == letter:
            output += 1
    return output

def checksum():
    duplicates = 0
    triplicates = 0
    for ID in boxIDs:
        hadDuplicate = 0
        hadTriplicate = 0
        for letter in getLetters(ID):
            checksumComp = countInstance(letter, ID)
            if checksumComp == 2:
                hadDuplicate = 1
            if checksumComp == 3:
                hadTriplicate = 1
        duplicates += hadDuplicate
        if hadDuplicate == 1: print(f"box {ID} had at least one duplicate!")
        triplicates += hadTriplicate
        if hadTriplicate == 1: print(f"box {ID} had at least one triplicate!")

    return duplicates * triplicates

print(f"Checksum: {checksum()}")
