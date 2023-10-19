import unittest

from lab3.src.find_successor import BinaryTree, find_successor, find_successor_second_idea

root = BinaryTree(10)
root.left = BinaryTree(5, parent=root)
root.right = BinaryTree(15, parent=root)
root.left.left = BinaryTree(3, parent=root.left)
root.left.right = BinaryTree(7, parent=root.left)
root.right.right = BinaryTree(20, parent=root.right)
root.right.right.left = BinaryTree(18, parent=root.right.right)


class FindSuccessorTest(unittest.TestCase):
    def test_case1(self):
        node = root.right
        successor = find_successor(root, node)
        self.assertEqual(successor.value, 18)

    def test_case2(self):
        node = root.left.right
        successor = find_successor(root, node)
        self.assertEqual(successor.value, 10)

    def test_case3(self):
        node = root.left.left
        successor = find_successor(root, node)
        self.assertEqual(successor.value, 5)

    def test_case4(self):
        node = root.left
        successor = find_successor(root, node)
        self.assertEqual(successor.value, 7)

    def test_case5(self):
        node = root
        successor = find_successor(root, node)
        self.assertEqual(successor.value, 15)

    def test_case6(self):
        node = root.right
        successor = find_successor_second_idea(root, node)
        self.assertEqual(successor.value, 18)

    def test_case7(self):
        node = root.left.right
        successor = find_successor_second_idea(root, node)
        self.assertEqual(successor.value, 10)

    def test_case8(self):
        node = root.left.left
        successor = find_successor_second_idea(root, node)
        self.assertEqual(successor.value, 5)

    def test_case9(self):
        node = root.left
        successor = find_successor_second_idea(root, node)
        self.assertEqual(successor.value, 7)

    def test_case10(self):
        node = root
        successor = find_successor_second_idea(root, node)
        self.assertEqual(successor.value, 15)


if __name__ == '__main__':
    unittest.main()
