class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    def assign_node(self, parent_node):
        if self.value >= parent_node.value:
            parent_node.right = self
            parent_node = self
            return
        else:
            parent_node.left = self
            parent_node = self
            return


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if arr == []:
        return None
    mid_point = arr[len(arr)//2]
    mid_index = len(arr)//2
    root = TreeNode(mid_point)

    root.left = arr_to_bst(arr[0:mid_index])
    root.right = arr_to_bst(arr[mid_index + 1::])

    return root
