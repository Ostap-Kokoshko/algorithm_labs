import unittest

from lab6.src.lab6 import finite_automata


class FiniteAutomataTest(unittest.TestCase):
    def test_1(self):
        pattern = "AB"
        text = "AAAAB"

        self.assertEqual([3], finite_automata(pattern, text))

    def test_2(self):
        pattern = "AAAA"
        text = "AB"

        self.assertEqual([], finite_automata(pattern, text))

    def test_3(self):
        pattern = " "
        text = "AAAAAB"

        self.assertEqual([], finite_automata(pattern, text))

    def test_4(self):
        pattern = "ABAB"
        text = "ABABABABABAB"

        self.assertEqual([0, 2, 4, 6, 8], finite_automata(pattern, text))


if __name__ == '__main__':
    unittest.main()
