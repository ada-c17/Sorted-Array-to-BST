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
    if len(arr) % 2 == 1:
        root_index = (len(arr) - 1) // 2
        root_node = TreeNode(arr[root_index])
    else:
        root_node = TreeNode(arr[len(arr) // 2])

    return root_node.val


print(arr_to_bst([1, 2, 3, 4]))
