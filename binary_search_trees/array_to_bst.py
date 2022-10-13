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

    mid_p = len(arr)//2
    root=TreeNode(arr[mid_p])

    root.left=arr_to_bst(arr[:mid_p])
    root.right=arr_to_bst(arr[mid_p+1:])

    return root