import unittest


from lab2.src.hamster_greed import max_hamsters_bst


class TestHamsterGreed(unittest.TestCase):

    def test_case_1(self):
        S = 30
        C = 5
        hamsters = [(2, 1), (4, 5), (3, 2), (6, 4), (1, 2)]
        self.assertEqual(max_hamsters_bst(S, C, hamsters), 3)

    def test_case_2(self):
        S = 7
        C = 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamsters_bst(S, C, hamsters), 2)

    def test_case_3(self):
        S = 19
        C = 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamsters_bst(S, C, hamsters), 3)

    def test_case_4(self):
        S = 2
        C = 2
        hamsters = [[1, 50000], [1, 60000]]
        self.assertEqual(max_hamsters_bst(S, C, hamsters), 1)

    def test_case_5(self):
        S = 7
        C = 3
        hamsters = [[1, 2], [3, 1], [2, 2]]
        self.assertEqual(max_hamsters_bst(S, C, hamsters), 2)

    def test_case_6(self):
        S = 5
        C = 1
        hamsters = [[5, 10000]]
        self.assertEqual(max_hamsters_bst(S, C, hamsters), 1)


if __name__ == "__main__":
    unittest.main()
