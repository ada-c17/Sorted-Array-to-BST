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
    
    # Recusive approach:
    # Find the middle index of the array
    mid = len(arr) // 2

    # Create a new root node with the value of mid
    root = TreeNode(arr[mid])

    # Left subtree has all the elements less than mid
    root.left = arr_to_bst(arr[:mid])
    # Right subtree has all the elements to greater or equal to mid
    root.right = arr_to_bst(arr[mid + 1:])

    return root
