import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()
    
    def test_empty(self):
        val = None

        act = self.s.reverseList(val)

        self.assertEqual(act, val)

        val = ListNode()

        act = self.s.reverseList(val)

        self.assertEqual(act, val)

    def test_simple(self):
        val = ListNode(0, ListNode(1))

        exp = ListNode(1, ListNode(0))

        act = self.s.reverseList(val)

        self.assertEqual(act, exp)

    def test_example(self):
        val = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        exp = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))

        act = self.s.reverseList(val)

        self.assertEqual(act, exp)