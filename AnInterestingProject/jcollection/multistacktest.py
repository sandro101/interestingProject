import unittest

from AnInterestingProject.jcollection.multistack import MultiStack
from AnInterestingProject.jcollection.stack import Stack


class StackTest(unittest.TestCase):
    def testPopWithConstructor(self):
        s = MultiStack("a", 0)
        s.push_at("b", 0)
        s.push_at("c", 1)
        s.push_at("d", 2)
        s.push_at("e", 0)
        self.assertEqual(s.pop_at(0), "e", "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop_at(2), "d", "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop_at(1), "c", "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop_at(0), "b", "Did not operate as stack, didn't give back last in")
        self.assertEqual(s.pop_at(0), "a", "Did not operate as stack, didn't give back last in")

        with self.assertRaises(ValueError):
            s.pop_at(0)
        with self.assertRaises(ValueError):
            s.pop_at(1)
        with self.assertRaises(ValueError):
            s.pop_at(2)
