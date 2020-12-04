import unittest
from ten import *

class TestPointsListMethods(unittest.TestCase):
    def setUp(self):
        self.l = PointsList("testInput.txt")

    def test_init(self):
        self.assertEqual(self.l.data[1], 'position=< 7,  0> velocity=<-1,  0>')
        self.assertEqual(self.l.data[4], 'position=< 2, -4> velocity=< 2,  2>')
        self.assertEqual(self.l.list[1].position, [7,0])
        self.assertEqual(self.l.list[1].velocity, [-1,0])
        self.assertEqual(self.l.numElements, 31)
        self.assertEqual(self.l.range, ((-6, 15), 21))
        # canvas should be empty
        self.assertEqual(self.l.canvas, [[]])

    def test_setUpCanvas(self):
        # canvas should exist and be filled with lots of ''
        self.assertEqual(self.l.canvas, [[]])
        self.l.setUpCanvas()
        self.assertEqual(self.l.canvas[1][1], '')

    def test_calculateRange(self):
        self.assertEqual(self.l.calculateRange(), ((-6, 15), 21))

    def test_moveAll(self):
        self.assertEqual(self.l.list[0].position, [9, 1])
        self.assertEqual(self.l.list[1].position, [7, 0])
        self.l.moveAll()
        self.assertEqual(self.l.list[0].position, [9, 3])
        self.assertEqual(self.l.list[1].position, [6, 0])

    def test_makePositive(self):
        self.assertEqual(self.l.range, ((-6, 15), 21))
        self.l.makePositive()
        self.assertEqual(self.l.range, ((0, 21), 21))

    def test_zero(self):
        self.assertEqual(self.l.range, ((-6, 15), 21))
        self.l.makePositive()
        self.assertEqual(self.l.range, ((0, 21), 21))
        self.l.moveAll()
        self.l.moveAll()
        self.l.moveAll()
        self.assertEqual(self.l.range, ((6, 15), 9))
        self.l.zero()
        self.assertEqual(self.l.range, ((1, 10), 9))

class TestRescuePointMethods(unittest.TestCase):
    def setUp(self):
        self.l = PointsList("testInput.txt")

    def test_move(self):
        self.assertEqual(self.l.list[0].position, [9, 1])
        self.l.list[0].move()
        self.assertEqual(self.l.list[0].position, [9, 3])

if __name__ == '__main__':
    unittest.main()
