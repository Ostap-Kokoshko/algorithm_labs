import unittest


from lab1.src.zigzag_function import zigzag_traversal
from lab1.src.zigzag_function import matrix


class TestZigzagTraversal(unittest.TestCase):

    def test_case_1(self):
        array1 = matrix(5, 5)
        self.assertEqual(zigzag_traversal(array1),
                         [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25])

    def test_case_2(self):
        array2 = matrix(2, 4)
        self.assertEqual(zigzag_traversal(array2), [1, 2, 5, 6, 3, 4, 7, 8])

    def test_case_4(self):
        self.assertEqual(zigzag_traversal(matrix(1, 1)), [1])

    def test_case_3(self):
        self.assertEqual(zigzag_traversal(matrix(1, 6)), [1, 2, 3, 4, 5, 6])

    def test_case_5(self):
        self.assertEqual(zigzag_traversal(matrix(6, 1)), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
