class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if not arr:
        return

    midpoint = len(arr) // 2

    node = TreeNode(value=arr[midpoint])
    node.left = arr_to_bst(arr[:midpoint])
    node.right = arr_to_bst(arr[midpoint+1:])

    return node