class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(root: BinaryTree, node: BinaryTree) -> BinaryTree:
    if root:
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor
        else:
            while node.parent and node == node.parent.right:
                node = node.parent
            return node.parent


def inorder_traversal(node):
    if node is None:
        return []

    result = []
    result += inorder_traversal(node.left)
    result.append(node.value)
    result += inorder_traversal(node.right)

    return result


def find_node_by_value(node, value):
    if node is None:
        return None
    if node.value == value:
        return node
    left_result = find_node_by_value(node.left, value)
    if left_result:
        return left_result
    return find_node_by_value(node.right, value)


def find_successor_second_idea(root, node):
    inorder = inorder_traversal(root)
    index = inorder.index(node.value)
    if index < len(inorder) - 1:
        successor_value = inorder[index + 1]
        return find_node_by_value(root, successor_value)
    else:
        return None
