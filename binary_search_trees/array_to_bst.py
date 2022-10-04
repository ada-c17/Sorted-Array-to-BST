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
    def make_tree(arr, node=None):
        if len(arr) < 1:
            return None
        elif len(arr) < 2:
            return TreeNode(arr[0])
        else:
            half = len(arr)//2
            if not node:
                node = TreeNode(arr[half])
            node.left = make_tree(arr[:half])
            node.right = make_tree(arr[half:])
    
    if len(arr) < 1:
        return None
    half = len(arr)//2
    root = TreeNode(arr[half])
    make_tree(arr, root)

    return root