import unittest
from solution import MyStack

class TestMyStack(unittest.TestCase):

    def setUp(self):
        self.stack = MyStack()

    def test_empty(self):
        self.assertEqual(True, self.stack.empty())

    def test_top(self):
        self.stack.push(2)

        self.assertEqual(2, self.stack.top())

        num = self.stack.pop()

        self.assertEqual(2, num)

    def test_multipush(self):
        for i in range(5):
            self.stack.push(i)
            self.assertEqual(self.stack.top(), i)


        for i in range(5):
            num = self.stack.pop()

            self.assertEqual(num, 5-i-1)