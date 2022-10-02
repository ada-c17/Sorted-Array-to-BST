class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def arr_to_bst_helper(arr, l_idx, r_idx):
    if l_idx == r_idx:
        return TreeNode(arr[l_idx])

    m_idx = int((l_idx + r_idx) / 2)
    tree = TreeNode(arr[m_idx])
    if m_idx > l_idx:
        tree.left = arr_to_bst_helper(arr, l_idx, m_idx-1)
    if m_idx < r_idx:
        tree.right = arr_to_bst_helper(arr, m_idx+1, r_idx)
    return tree


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if arr == None or len(arr) == 0:
        return None
    
    return arr_to_bst_helper(arr, 0, len(arr)-1)

# a = [5, 10, 15]
# tree = arr_to_bst(a)