class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def arr_to_bst(arr):       
    def helper(left, right):
        if left > right:
            return None

        # always choose left middle node as a root
        p = (left + right) // 2

        # preorder traversal: node -> left -> right
        root = TreeNode(arr[p])
        root.left = helper(left, p - 1)
        root.right = helper(p + 1, right)
        return root
    
    return helper(0, len(arr) - 1)