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
    #base case #1
    if len(arr) == 0:
      return None
    #base case #2 
    elif len(arr) == 1:
      return TreeNode(arr[0])
    else:
      mid_root_index = len(arr) // 2
      #creatung a BST where root is the mid number of list input
      root = TreeNode(arr[mid_root_index])

      #splitting list input into left/right lists via list slicing 
      left_list = arr[:mid_root_index]
      right_list = arr[mid_root_index + 1:]

      #recurisvely calling arr_to_bst until list is len of 1, when we have leaf nodes
      root.left = arr_to_bst(left_list)
      root.right = arr_to_bst(right_list)
      return root

