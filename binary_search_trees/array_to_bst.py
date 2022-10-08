class TreeNode:
    def __init__(self, value, left=None, right=None):
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

    return recursive_helper(arr)


def recursive_helper(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return TreeNode(arr[0])

    mid = len(arr) // 2

    if len(arr) == 2:
        sub_array = []
    elif len(arr) == 3:
        sub_array = [arr[-1]]
    else:
        sub_array = arr[mid+1:]

    node = TreeNode(arr[mid],
                    recursive_helper(arr[:mid]),
                    recursive_helper(sub_array))

    return node
