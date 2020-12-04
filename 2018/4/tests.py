import unittest
from four import *

class TestEntryListMethods(unittest.TestCase):
    def setUp(self):
        self.e = EntryList("testInput.txt")
        self.e.load()

    def test_calculateGuardSleep(self):
        self.assertEqual(self.e.calculateGuardSleep(10), 50)
        self.assertEqual(self.e.calculateGuardSleep(99), 30)

    def test_findSleepiestGuard(self):
        self.assertEqual(self.e.findSleepiestGuard(), 10)

    def test_findSleepyMinute(self):
        self.assertEqual(self.e.findSleepyMinute(10), 24)
        self.assertEqual(self.e.findSleepyMinute(99), 45)

    def test_solve(self):
        self.assertEqual(self.e.solve(), (240, 4455))

    def test_findMostSleptMinute(self):
        self.assertEqual(self.e.findMostSleptMinute(), (99, 45))

if __name__ == '__main__':
    unittest.main()
