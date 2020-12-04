import sys
sys.path.append('../')

from list import *

class NoSuchChildException(Exception):
    pass

HEADER_LENGTH = 2

class LNTree:
    def __init__(self, children, metadata, length):
        self.children = children
        self.metadata = metadata
        self.length = length

    # returns the specified child node, 0-indexed
    def getChildByNumber(self, number):
        try:
            return self.children[number]
        except Exception as e:
            raise NoSuchChildException

    def __str__(self):
        children = ''
        for child in self.children:
            children += str(child)
        return ' {' + str(children) + '} ' + str(self.metadata)
        # return str(self.children) + str(self.metadata)

    def sumMetadata(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        else:
            total = 0
            for child in self.children:
                total += child.sumMetadata()
            return sum(self.metadata) + total

    def calculateValue(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        else:
            value = 0
            for entry in self.metadata:
                try:
                    print(f'self.children: {self.children}')
                    print(f'self.metadata: {self.metadata}')
                    print(f'entry-1: {entry-1}')
                    childFromMetadata = self.children[entry-1]
                    value += childFromMetadata.calculateValue()
                except:
                    print("SKIPPED")
            return value


class LicenseNumber(List):
    def __init__(self, file):
        super().__init__(file)
        with open(self.fileName) as input:
            self.data = list(map(int, input.read().split()))

    # returns tree of the license number with each node a LNTree object
    def makeTree(self, ln, nodeStart):
        header = ln[nodeStart:nodeStart+2]

        numberOfChildren = ln[nodeStart]
        metadataLength = ln[nodeStart+1]

        # if this node has no children, just return the node with its header and metadata
        if numberOfChildren == 0:
            metadata = ln[nodeStart + HEADER_LENGTH:nodeStart + HEADER_LENGTH + metadataLength]
            print(f'metadata: {metadata}')
            return LNTree([], metadata, HEADER_LENGTH + metadataLength)
        else:
            children = []
            currentChildNodeStart = HEADER_LENGTH+nodeStart
            for child in range(numberOfChildren):
                currentChild = self.makeTree(ln, currentChildNodeStart)
                children.append(currentChild)
                currentChildNodeStart += currentChild.length
            # metadata is always the last x digits of the node where x is the
            # amount of metadata defined in the header
            allChildrenLength = currentChildNodeStart - nodeStart - HEADER_LENGTH
            metadataStart = nodeStart+HEADER_LENGTH + allChildrenLength
            metadata = ln[metadataStart:metadataStart + metadataLength]
            print('\nPARSING!')
            print(' '.join(str(e) for e in ln))
            print(f'nodeStart: {nodeStart}')
            print(f'header: {header}')
            print(f'allChildrenLength: {allChildrenLength}')
            print(f'numberOfChildren: {numberOfChildren}')
            print(f'metadataLength: {metadataLength}')
            print(f'metadataStart: {metadataStart}')
            print(f'metadata: {metadata}')
            return LNTree(children, metadata, HEADER_LENGTH+allChildrenLength+metadataLength)

if __name__ == '__main__':
    a = LicenseNumber("input.txt")
    t = a.makeTree(a.data, 0)
    print(f't: {t}')
    print(t.sumMetadata())
    print(t.calculateValue())
