import unittest
from AnInterestingProject.jcollection.queue import Queue


class QueueTest(unittest.TestCase):
    def testPopWithConstructor(self):
        q = Queue(0)
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 0, "Did not operate as queue, didn't give back first in")

    def testPopDownToLastElement(self):
        q = Queue(0)
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 0, "Did not operate as queue, didn't give back first in")
        self.assertEqual(q.pop(), 1, "Did not operate as queue, didn't give back first in")
        self.assertEqual(q.pop(), 2, "Did not operate as queue, didn't give back first in")
        self.assertEqual(q.pop(), 3, "Did not operate as queue, didn't give back first in")
        with self.assertRaises(ValueError):
            q.pop()

    def testPopDownAndFillBackUp(self):
        q = Queue(0)
        q.push(1)
        self.assertEqual(q.pop(), 0, "Did not operate as queue, didn't give back first in")
        self.assertEqual(q.pop(), 1, "Did not operate as queue, didn't give back first in")
        with self.assertRaises(ValueError):
            q.pop()
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 2, "Did not operate as queue, didn't give back first in")
        self.assertEqual(q.pop(), 3, "Did not operate as queue, didn't give back first in")