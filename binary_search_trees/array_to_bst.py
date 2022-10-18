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

    elif len(arr) == 1:
        return TreeNode(arr[0])

    return TreeNode(arr[(len(arr) // 2)], arr_to_bst(arr[:(len(arr) // 2)]), arr_to_bst(arr[((len(arr) // 2)+1):]))
