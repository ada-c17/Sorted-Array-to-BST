class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def bst_helper(arr):
    if arr:
        this_node_index = len(arr) // 2
        this_node_val = arr[this_node_index]
        left_array = arr[0:this_node_index]
        right_array = arr[(this_node_index + 1):]
        left_node = bst_helper(left_array)
        right_node = bst_helper(right_array)

        result = TreeNode(this_node_val, left_node, right_node)
        return result
    else:
        return None

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    return bst_helper(arr)
