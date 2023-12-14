import unittest

from lab7.src.ijones import ijones


class MyTestCase(unittest.TestCase):
    def test_indiana_jones_case1(self):
        matrix = [['a', 'a', 'a'],
                  ['c', 'a', 'b'],
                  ['d', 'e', 'f']]
        result = ijones(matrix, 3, 3)
        expected_result = 5
        self.assertEqual(result, expected_result)

    def test_indiana_jones_case2(self):
        matrix = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]
        result = ijones(matrix, 1, 10)
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_indiana_jones_case3(self):
        matrix = [['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
                  ['a', 'a', 'a', 'a', 'a', 'a', 'a']]
        result = ijones(matrix, 6, 7)
        expected_result = 201684
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
