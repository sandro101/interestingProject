import unittest
from AnInterestingProject.jcollection.stack import Stack


class StackTest(unittest.TestCase):
    def testPopWithConstructor(self):
        s = Stack(0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")

    def testPopDownToLastElement(self):
        s = Stack(0)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 2, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 1, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 0, "Did not operate as stack, didn't give back last in")
        with self.assertRaises(ValueError):
            s.pop()

    def testPopDownAndFillBackUp(self):
        s = Stack(0)
        s.push(1)
        self.assertEqual(s.pop(), 1, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 0, "Did not operate as stack, didn't give back last in")
        with self.assertRaises(ValueError):
            s.pop()
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop(), 2, "Did not operate as stack, didn't give back last in")