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
    if len(arr) == 0:
        return None
        
    middle_index = len(arr) // 2
    left = arr_to_bst(arr[0: middle_index])
    right = arr_to_bst(arr[middle_index + 1:])

    root_node = TreeNode(arr[middle_index], left, right)

    return root_node