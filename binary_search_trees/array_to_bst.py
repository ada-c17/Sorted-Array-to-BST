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
    
    def portion_arr(left_arr, right_arr):
        if left_arr > right_arr: 
            return None
        
        mid_arr = (left_arr + right_arr) // 2
        root = TreeNode(arr[mid_arr])
        root.left = portion_arr(left_arr, mid_arr - 1)
        root.right = portion_arr(mid_arr + 1, right_arr)
        return root

    return portion_arr(0, len(arr) - 1)