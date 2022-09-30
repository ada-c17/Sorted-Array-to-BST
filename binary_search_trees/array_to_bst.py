class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def find_middle(arr):
    list_length = len(arr)
    mid_index = list_length // 2
    return mid_index


def arr_to_bst(arr):
    if not arr:
        return None
    mid_index = find_middle(arr)
    root = TreeNode(arr[mid_index])

    root.left = arr_to_bst(arr[:mid_index])
    root.right = arr_to_bst(arr[mid_index + 1:])
    return root
