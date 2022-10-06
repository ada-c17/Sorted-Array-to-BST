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

    #helper function to handle recursion
    # pick middle element in list
    # set middle element to root
    # grab left list
    # grab right list
    #assign left side to recersive call of left list (root.left)

    pass