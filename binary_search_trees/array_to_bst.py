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

    mid_node = len(arr)//2
    node = TreeNode(arr[mid_node])
    node.left = arr_to_bst(arr[:mid_node])
    node.right = arr_to_bst(arr[mid_node+1:])
    return node