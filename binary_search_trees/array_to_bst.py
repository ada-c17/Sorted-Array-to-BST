class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


# arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if not arr:
        return None
    # get the middle index, set as root
    mid_index = len(arr)//2
    root = TreeNode(arr[mid_index])
    # while there is something to the left of the index
        # set nodes for the left
        # the return None on line 16 stops this
    root.left = arr_to_bst(arr[:mid_index])
    
    # while there is something to the right of the index
        # set nodes for the right
    root.right = arr_to_bst(arr[mid_index+1:])

    return root
    
