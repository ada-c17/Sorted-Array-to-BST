class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def recursive_helper(arr):
    if len(arr) == 1:
        return TreeNode(arr[0])

    new_node_index = len(arr)//2

    new_node = TreeNode(arr[new_node_index])

    new_node.left = recursive_helper(arr[:new_node_index])

    if len(arr) > new_node_index + 1 :
        new_node.right = recursive_helper(arr[new_node_index::])

    return new_node

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if not arr:
        return None
    
    return recursive_helper(arr)




# import in test file wasn't working, so brought these functions into main module to test
def is_bst(root):
    if root is None:
        return True

    left = root.left
    if left is not None and root.val <= left.val:
        return False

    right = root.right
    if right is not None and root.val >= right.val:
        return False

    return is_bst(left) and is_bst(right)

# Returns the height of a tree
def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


# Returns True if a tree is balanced
def is_balanced_tree(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    left_check = is_balanced_tree(root.left)
    right_check = is_balanced_tree(root.right)

    return left_check and right_check

array = [1, 2, 3, 4, 5]

middle_node = arr_to_bst(array)

print(is_bst(middle_node))
print(is_balanced_tree(middle_node))



