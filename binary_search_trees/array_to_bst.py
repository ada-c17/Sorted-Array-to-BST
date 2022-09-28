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

    middle = len(arr)//2
    root_node = TreeNode(arr[middle])


    root_node.left = arr_to_bst(arr[:middle])
        
    root_node.right = arr_to_bst(arr[middle+1:])

    return root_node
