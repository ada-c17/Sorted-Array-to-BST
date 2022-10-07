class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root):
        self.root = root


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if not arr:
        return None

    mid_index = len(arr)//2
    midpoint = arr[mid_index]
    node = TreeNode(midpoint)
    node.left = arr_to_bst(arr[0:mid_index])
    node.right = arr_to_bst(arr[mid_index + 1:])

    return node
