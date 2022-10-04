from hashlib import new


class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def helper(arr, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    new_node = TreeNode(arr[mid])
    new_node.left = helper(arr, left, mid-1)
    new_node.right = helper(arr, mid+1, right)
    return new_node

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    # if arr is empty, return None
    if not arr:
        return None

    return helper(arr, 0, len(arr)-1)