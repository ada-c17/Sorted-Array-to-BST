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
    #helper function to handle tree build recursively ✅
    # empty list return None ✅
    # pick middle element in list ✅
    # set middle element to root ✅
    # grab left list ✅
    # grab right list ✅


    #assign left side to recersive call of left list (root.left)
    if not arr:
        return None
    # pick middle of list with length of array and floor division
    middle = len(arr) // 2
    # set middle element to root
    root = TreeNode(arr[middle])
    # set left root node to anything less than the middle
    # use indexing to consider everything less than the middle, recursively
    root.left = arr_to_bst(arr[:middle])
    # set the right root node to anything greater than the middle
    # indexing to consider everything starting at one greater than the middle, recursively
    root.right = arr_to_bst(arr[middle+1:])
    return root
    
    
def tree_helper(node):
    if not node:
        return
    tree_helper(node.left)
    tree_helper(node.right)
