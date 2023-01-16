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
    middle_num = len(arr) // 2
    left_side = arr_to_bst(arr[:middle_num])
    right_side = arr_to_bst(arr[middle_num + 1:])
    return TreeNode(arr[middle_num], left_side, right_side)