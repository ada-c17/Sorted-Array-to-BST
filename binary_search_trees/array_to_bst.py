class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


# This is a solution I found online that makes most sense to me
# source: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.php
# I couldn't figure out a solution on my own, my approach (where I ultimately got stuck) is commented out below.

def arr_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums)//2
    node = TreeNode(array_nums[mid_num])
    node.left = arr_to_bst(array_nums[:mid_num])
    node.right = arr_to_bst(array_nums[mid_num+1:])
    return node


def arr_to_bst_mine(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    # middle of array becomes root node
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return TreeNode(arr[0])
    else:
        middle=arr[len(arr)//2]
        root_node = TreeNode(middle)
        root_node.left = arr_to_bst_helper_mine()
        return root_node

def arr_to_bst_helper_mine(current_value, arr):
    if arr == []:
        return None
    new_node = TreeNode(current_value)

    # is there nothing to the left of the node
    current_idx = arr.index(current_value)
    if current_idx == 0:
        new_node.left = None
    else:
        middle_left = (current_idx - 1) // 2
        new_node.left = arr_to_bst_helper_mine(arr[middle_left], arr)

    # is there nothing to the right of the node
    current_idx = arr.index(current_value)
    if current_idx == len(arr) - 1:
        new_node.right = None
    else:
        middle_right = current_idx + 1 + (len(arr) - 1 - current_idx) // 2
        new_node.right = arr_to_bst_helper_mine(arr[middle_right], arr)
    
    return new_node

arr_to_bst([1,2,3])
