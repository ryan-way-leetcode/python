import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()


    def test_example1(self):

        test = [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
                ListNode(2, ListNode(6)),
        ]

        exp = ListNode(1, 
                ListNode(1, 
                    ListNode(2, 
                        ListNode(3, 
                            ListNode(4, 
                                ListNode(4, 
                                    ListNode(5, 
                                        ListNode(6))))))))

        act = self.s.mergeKLists(test)

        while act is not None and exp is not None:
            self.assertEqual(exp.val, act.val)

            exp, act = exp.next, act.next

        if act is None and exp is None:
            return
        else:
            self.assertTrue(False)
