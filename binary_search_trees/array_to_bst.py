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
    # If array is empty
    if not arr:
        return None
    
    # Find the middle element and make it the root node
    # Want to repeat this for the left and right subtrees
    mid_ind = (len(arr)) // 2
    root = TreeNode(arr[mid_ind])

    # Left subtree
    root.left = arr_to_bst(arr[:mid_ind])

    # Right subtree
    # +1 so we don't include the current mid in the next call
    root.right = arr_to_bst(arr[mid_ind + 1:])

    return root