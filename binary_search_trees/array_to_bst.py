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
        return

    total_lenght = len(arr)
    middle_node = total_lenght // 2
    return TreeNode(arr[middle_node], arr_to_bst(arr[:middle_node]), arr_to_bst(arr[middle_node+1:]))