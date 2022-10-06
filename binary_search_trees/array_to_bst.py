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
    elif len(arr) == 1:
        return TreeNode(arr[0])
    else:
        arr_midpoint = len(arr) // 2
        midpoint_node = TreeNode(arr[arr_midpoint])
        left_arr = arr[0:arr_midpoint]
        right_arr = arr[arr_midpoint+1:len(arr)]
        midpoint_node.right = arr_to_bst(right_arr)
        midpoint_node.left = arr_to_bst(left_arr)
        print(midpoint_node.val)
        return midpoint_node

