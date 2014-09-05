__author__ = 'ipetrash'

import unittest

# TODO: добавить тест, ваш кэп.
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_1(self):
        self.assertEqual(True, True)
    def test_foo(self):
        self.assertEqual(False, False)

if __name__ == '__main__':
    unittest.main()
