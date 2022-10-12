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

    # Find middle of array and set as root node
    root_index = len(arr) // 2
    root_node = TreeNode(arr[root_index])

    # Create left and right subtrees
    root_node.left = arr_to_bst(arr[:root_index])
    root_node.right = arr_to_bst(arr[root_index+1:])

    return root_node

# Notes:
# If middle element in a sorted array is the root of the tree, than the first half of the array
# can go to the left, and the second half to the right, and the tree will be balanced.