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
    # base case: if the input array is empty, return None
    if not arr:
        return None
    # Find the middle element of the array
    mid = len(arr) // 2
    # Create a new TreeNode with the middle element as the value
    root = TreeNode(arr[mid])
    # Recursively call the function for the left sub-array and assign the returned value as the left child of the root node
    root.left = arr_to_bst(arr[:mid])
    # Recursively call the function for the right sub-array and assign the returned value as the right child of the root node
    root.right = arr_to_bst(arr[mid+1:])
    # return the root of the balanced BST
    return root
