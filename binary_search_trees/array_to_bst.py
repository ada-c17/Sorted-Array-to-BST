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
    ## recommended to make problem recursive starting at the middle of the list
    # create a root node with the middle element in the list
    # check the second element in the list
    # if that element is larger or equal to the root:
    # that element becomes the left child node
    # if that element is smaller or equal to the root:
    # that element becomes the right child node
    pass