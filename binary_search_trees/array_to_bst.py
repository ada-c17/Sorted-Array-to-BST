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
    def convert(l, r):
        if l > r:
            return None
    
        m = l + (r - l) // 2
        root = TreeNode(arr[m])
        root.left = convert(l, m - 1)
        root.right = convert(m + 1, r)
        return root

    return convert(0, len(arr) - 1)