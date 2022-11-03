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
    #base case
    if not arr:
        return None
    #find the middle 
    mid = len(arr) // 2
    #create a node with the middle element
    #and recursively create the left and right subtrees
    #using the left and right halves of the array
    return TreeNode(arr[mid], arr_to_bst(arr[:mid]), arr_to_bst(arr[mid + 1:]))