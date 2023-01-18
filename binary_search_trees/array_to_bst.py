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
        return None

    half = (len(arr)) // 2
    current = TreeNode(arr[half])

    current.left = arr_to_bst(arr[:half])
    current.right = arr_to_bst(arr[half+1:])

    return current