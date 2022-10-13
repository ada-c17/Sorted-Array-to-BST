
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

    # def __repr__(self):
    #     return 'TreeNode(' + repr(self.val) + ", left: " + repr(self.left) + ", right: " + repr(self.right) + ")"


def arr_to_bst(arr):
    if not arr:
        return None
    elif len(arr) == 1:
        return TreeNode(arr[0])

    mid_index = len(arr) // 2
    return TreeNode(arr[mid_index], arr_to_bst(arr[:mid_index]), arr_to_bst(arr[mid_index+1:]))

root = arr_to_bst([5, 10, 15, 20, 25, 30, 35, 40, 45])
# print(repr(root))
# print(root.left.left.left.val)