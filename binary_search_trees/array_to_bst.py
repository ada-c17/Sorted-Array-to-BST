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

    # return None if array is empty
    if len(arr) == 0:
        return None
    
    # finding mid pointer
    mid = len(arr) // 2
    # creating root of Node
    root = TreeNode(arr[mid])
    # creating left subtree of tree recursively
    root.left = arr_to_bst(arr[:mid])
    # creating right subtree of tree recursively
    root.right = arr_to_bst(arr[mid + 1:])
    return root