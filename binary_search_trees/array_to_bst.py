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
    inorder_array = []
    if not arr:
        return None

    middle = len(arr)//2
    root_node = TreeNode(arr[middle])

    arr_to_bst(root_node.left)
    inorder_array.append(root_node.val)
    arr_to_bst(root_node.left)

    return root_node
