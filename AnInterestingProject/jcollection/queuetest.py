import unittest
from jcollection.queue import Queue


class QueueTest(unittest.TestCase):
    def testPopWithConstructor(self):
        q = Queue(0)
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 0, "Popped one value lived up to FIFO")
