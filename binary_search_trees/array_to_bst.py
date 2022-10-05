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
    '''
    1. Recursivley assign root to be whatever you get returned for left/right side of the list. 
    2. Function takes in list. 
        a. Assign left to be middle of left list. 
        b. Assign right to middle of right list. 
        root.left = arr_to_bst(left_side)
        root.right = arr_to_bst(right_side)
        return root
    '''
    if not arr:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    # if not root.left: # May not need this
        # Call function again, but only with left side of list
    root.left = arr_to_bst(arr[:mid]) # Assign root.left and root.right to be these values
    # if not root.right:
    root.right = arr_to_bst(arr[mid + 1:]) # Only want to grab mid + 1
    # Consider returning something at the end (root of tree)
    return root