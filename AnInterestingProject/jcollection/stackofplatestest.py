import unittest
from AnInterestingProject.jcollection.stackofplates import StackOfPlates


class StackOfPlatesTest(unittest.TestCase):
    def testPopWithConstructor(self):
        s = StackOfPlates(0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")

    def testPopDownToLastElement(self):
        s = StackOfPlates(0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 2, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 1, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 0, "Did not operate as stack, didn't give back last in")
        with self.assertRaises(ValueError):
            s.pop()

    def testPopDownThenPushBackUpAgainThenEmpty(self):
        s = StackOfPlates(0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 2, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 1, "Did not operate as stack, didn't give back last in")
        s.push(4)
        s.push(5)
        s.push(6)
        s.push(7)
        s.push(8)
        s.push(9)
        s.push(10)
        self.assertEqual(s.pop(), 10, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 9, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 8, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 7, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 6, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 5, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 4, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 0, "Did not operate as stack, didn't give back last in")
        with self.assertRaises(ValueError):
            s.pop()

    def testPopDownAndFillBackUp(self):
        s = StackOfPlates(0)
        s.push(1)
        self.assertEqual(s.pop(), 1, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 0, "Did not operate as stack, didn't give back last in")
        with self.assertRaises(ValueError):
            s.pop()
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 2, "Did not operate as stack, didn't give back last in")