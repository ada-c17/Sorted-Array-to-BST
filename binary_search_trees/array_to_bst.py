class TreeNode:
    def __init__(self, value, left=None, right=None):
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

    if len(arr) == 1:
        return TreeNode(arr[0])

    mid_idx = len(arr)//2
    root = TreeNode(arr[mid_idx])

    root.left = arr_to_bst(arr[0:mid_idx])
    root.right = arr_to_bst(arr[mid_idx+1:])

    return root
