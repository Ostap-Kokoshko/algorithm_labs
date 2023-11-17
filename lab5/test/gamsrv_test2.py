import unittest
from lab5.src.newf import find_minimum_latency


class TestGamsrv(unittest.TestCase):
    def test_case1(self):
        lines = [
            "6 6",
            "1 2 6",
            "1 3 10",
            "3 4 80",
            "4 5 50",
            "5 6 20",
            "2 3 40",
            "2 4 100"
        ]
        expected = 100
        actual = find_minimum_latency(lines)
        self.assertEqual(expected, actual)

    def test_case2(self):
        lines = [
            "9 12",
            "2 4 6",
            "1 2 20",
            "2 3 20",
            "3 6 20",
            "6 9 20",
            "9 8 20",
            "8 7 20",
            "7 4 20",
            "4 1 20",
            "5 2 10",
            "5 4 10",
            "5 6 10",
            "5 8 10"
        ]
        expected = 10
        actual = find_minimum_latency(lines)
        self.assertEqual(expected, actual)

    def test_case3(self):
        lines = [
            "3 2",
            "1 3",
            "1 2 100",
            "3 2 200"
        ]
        expected = 200
        actual = find_minimum_latency(lines)
        self.assertEqual(expected, actual)

    def test_case4(self):
        lines = [
            "5 8",
            "1 2 4 5",
            "1 2 20",
            "2 4 20",
            "4 5 20",
            "5 1 20",
            "1 3 10",
            "2 3 10",
            "3 4 10",
            "3 5 10"
        ]
        expected = 10
        actual = find_minimum_latency(lines)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()