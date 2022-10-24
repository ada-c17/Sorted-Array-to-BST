class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def helper(arr, root):

    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2 #finds middle point
    #Gets the middle number and creates the root for the child and keeps going left
    root.left = helper(arr[:mid], TreeNode(arr[mid])) 
    #Gets the middle number and creates the root for the child and keeps going right
    root.right = helper(arr[mid:], TreeNode(arr[mid]))



def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """

    if not arr:
        return None

    mid = len(arr)//2
    root = TreeNode(arr[mid])

    helper(arr, root)
    return root