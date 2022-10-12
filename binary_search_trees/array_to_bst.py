class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def helper(arr, lower, upper):
    if lower == upper:
        return None

    mid = (lower + upper) // 2
    node = TreeNode(arr[mid])
    node.left = helper(arr, lower, mid)
    node.right = helper(arr, mid + 1, upper)
    return node


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    return helper(arr, 0, len(arr))
