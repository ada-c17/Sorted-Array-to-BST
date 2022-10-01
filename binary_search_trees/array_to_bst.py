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
    
    mid = (len(arr)) // 2

    # set middle element of array as root
    root = TreeNode(arr[mid])

    # recursively get the middle of the left half and make it the left child of the root created
    root.left = arr_to_bst(arr[:mid])
    # recursively get the middle of the right half and make it the right child of the root created
    root.right = arr_to_bst(arr[mid+1:])

    # return root of the finished tree
    return root