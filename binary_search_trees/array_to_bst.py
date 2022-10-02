class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


#PSEUDOCODE
# get the middle of array-> set it equal to root of tree
# get the middle of the left half of array  and make it equal to the root.left value
# get middle of right half of array and make it equal to root.right value

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if  not arr:
        return None
    midpoint = len(arr)//2
    root = TreeNode(arr[midpoint])
    root.left = arr_to_bst(arr[:midpoint])
    root.right = arr_to_bst(arr[midpoint + 1:])
    return root