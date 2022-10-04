class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def arr_to_bst(arr):
    if not arr:
        return None

    middle =(len(arr)) // 2

    # make the middle element the root
    root = TreeNode(arr[middle])
    
    root.left = arr_to_bst(arr[:middle])
    
    root.right = arr_to_bst(arr[middle+1:])
    return root

