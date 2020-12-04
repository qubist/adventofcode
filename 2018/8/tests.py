import unittest
from eight import *

class TestLicenseNumberMethods(unittest.TestCase):
    def setUp(self):
        self.a = LicenseNumber("testInput.txt")

    def test_init(self):
        self.assertEqual(self.a.data, [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])

    # def test_convertToTree(self):
    #     t = self.a.makeTree()
    #     # root node "A" has header 2 3
    #     self.assertEqual(t.header, [2, 3])
    #     # children and metadata arrays match the header
    #     self.assertEqual(len(t.children), 2)
    #     self.assertEqual(len(t.metadata), 3)
    #     # node "B" has header 0 3
    #     self.assertEqual(t.getChildByNumber(0).header, [0,3])
    #     # node "B" has first metadata item 10
    #     self.assertEqual(t.getChildByNumber(0).metadata[0], 10)

    def test_makeTree(self):
        self.t = self.a.makeTree(self.a.data, 0)
        self.assertEqual([1,1,2],self.t.metadata)
        self.assertEqual(self.t.children[0].metadata, [10,11,12])
        self.assertEqual(len(self.t.children),2)

    def test_sumMetadata(self):
        self.t = self.a.makeTree(self.a.data, 0)
        self.assertEqual(self.t.sumMetadata(), 138)

    def test_calculateValue(self):
        self.t = self.a.makeTree(self.a.data, 0)
        self.assertEqual(self.t.children[0].calculateValue(), 33)
        self.assertEqual(self.t.calculateValue(), 66)

if __name__ == '__main__':
    unittest.main()
