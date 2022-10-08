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
    # find the middle point and make it as the root
    mid = (len(arr)) // 2
    root = TreeNode(arr[mid])
    # values less than mid should go to left side
    root.left = arr_to_bst(arr[:mid])
    # values larger than mif should go to right side
    root.right = arr_to_bst(arr[mid+1:])
    return root


