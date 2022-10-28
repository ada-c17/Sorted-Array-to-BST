class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    """
    1. Find the middle index of the given array
    2. Make the root of the BST to be the middle element
    3. Use recursion to find the middle of the left half of the array and use it as the left child and so on
    4. Same for the right half, find the middle of the remaining array elements on the right, and set it as right child of the root

    Time Complexity: O(N) 
    Space Complexity: O(H) = O(log(N)), for recursive stack space where H is the height of the tree.
    """
    if not arr:
        return None

    mid = (len(arr)) // 2
    root = TreeNode(arr[mid])

    root.left = arr_to_bst(arr[:mid])
    root.right = arr_to_bst(arr[mid + 1:])

    return root