class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.

        arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    """
    if not arr:
        return None
    
    middle = len(arr) // 2

    root = TreeNode(arr[middle])

    root.left = arr_to_bst(arr[:middle])
    root.right = arr_to_bst(arr[middle+1:])

    return root