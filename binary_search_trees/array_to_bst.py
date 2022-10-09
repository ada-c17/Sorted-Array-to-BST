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
    return tree_helper(arr) 


def tree_helper(arr):
    if not arr:
        return None
        
    node_index = len(arr)//2
    val = arr[node_index]
    l_tree = arr[0:node_index]
    r_tree = arr[node_index+1:]
    l = tree_helper(l_tree)
    r = tree_helper(r_tree)
    
    return TreeNode(val, l, r)