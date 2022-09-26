from os import spawnl


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
    # [5, 10, 15, 20, 25, 30, 35, 40, 45]
    # STEP 0: initialize left_side and right_side variables
    # STEP 1: find middle, set variable to sides
        # left_side = [5, 10, 15, 20, 25]
        # right_side = [30, 35, 40, 45]
    # STEP 2: If not odd, go to left for root
        # left_side = [5, 10, 15, 20]
        # right_side = [30, 35, 40, 45]
    # STEP 3: Set root
        # root = 25
    # STEP 4: RECURSION - for LEFT
        # see STEP 1-ish
        # left side -- to the left
            # [5, 10]
            # current.left = 10
        # see STEP 1-ish
        # left side -- to the left
            # [5]
            # current.left = 5
    # STEP 4: RECURSION - for RIGHT
        # see STEP 1-ish
        # right side -- to the right
            # [5, 10]
            # current.right = 10
        # see STEP 1-ish
        # right side -- to the right
            # [5]
            # current.right = 5

    # half = round(len(arr)/2)
    if not arr:
        return None

    half = (len(arr)) // 2
    current = TreeNode(arr[half])

    current.left = arr_to_bst(arr[:half])
    current.right = arr_to_bst(arr[half+1:])

    return current
    
