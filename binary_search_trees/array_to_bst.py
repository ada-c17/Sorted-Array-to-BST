from tkinter.tix import Tree


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
    # # approach 1:
    # if not arr or len(arr) == 0:
    #     return
    # mid = len(arr)//2
    # root = TreeNode(arr[mid])
    # root.right = arr_to_bst(arr[mid+1:])
    # root.left = arr_to_bst(arr[:mid])
    # return root

    # approach 2 (avoid slicing as expensive):
    if not arr:
        return
    return arr_to_bst_helper(arr, 0, len(arr)-1)

# approach 2 (avoid slicing as expensive): 
def arr_to_bst_helper(arr, start, end):
    if start == end:
        return TreeNode(arr[start])
    elif start < end:
        mid = (start + end)//2
        root = TreeNode(arr[mid])
        root.left = arr_to_bst_helper(arr, start, mid-1) #inclusive
        root.right = arr_to_bst_helper(arr, mid+1, end) #inclusive
        return root