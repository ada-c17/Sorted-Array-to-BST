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
    if not arr:  # if the arr is empty return none 
        return None
    mid = len(arr) // 2 # find the middle index
    root = TreeNode(arr[mid]) #because we know the array is sorted we know the middle number is the tree node and will use this as the root 
    root.left = arr_to_bst(arr[:mid])
    root.right = arr_to_bst(arr[mid+1:])

    return root