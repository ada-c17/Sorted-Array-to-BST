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
    mid = len(arr)//2
    root = helper(arr, 0, len(arr))
    return root

def helper(arr, start, end):
    if start < end:
        mid = (start+end)//2
        root = TreeNode(value=arr[mid])
        root.left = helper(arr, start, mid-1)
        root.right = helper(arr, mid+1, end)
        return root