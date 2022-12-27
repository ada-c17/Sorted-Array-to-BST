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
    def returnOddVals(arr):
        mid_index = len(arr)//2
        return arr[mid_index], arr[:mid_index], arr[mid_index+1:]
    
    def returnEvenVals(arr):
        mid_index = len(arr)//2-1
        return arr[mid_index], arr[:mid_index], arr[mid_index+1:]

    def recursive_helper(prev, left_side, right_side):
        #left side
        if not left_side:
            new_node_val = None
        elif len(left_side) == 1:
            new_node_val = left_side[0]
            new_left_node = TreeNode(new_node_val)
            prev.left = new_left_node
        else:
            if len(left_side)%2 == 0:
                new_node_val, new_left_for_left_side, new_right_for_left_side = returnEvenVals(left_side)
            else:
                new_node_val, new_left_for_left_side, new_right_for_left_side = returnOddVals(left_side)
            if new_node_val:
                new_left_node = TreeNode(new_node_val)
            else:
                new_left_node = None
            prev.left = new_left_node
            recursive_helper(new_left_node, new_left_for_left_side, new_right_for_left_side)

        #right side
        if not right_side:
            new_node_val = None
        elif len(right_side) == 1:
            new_node_val = right_side[0]
            new_right_node = TreeNode(new_node_val)
            prev.right = new_right_node
        else:
            if len(right_side)%2 == 0:
                new_node_val, new_left_for_right_side, new_right_for_right_side = returnEvenVals(right_side)
            else:
                new_node_val, new_left_for_right_side, new_right_for_right_side = returnOddVals(right_side)
            if new_node_val:
                new_right_node = TreeNode(new_node_val)
            else:
                new_right_node = None
            prev.right = new_right_node
            recursive_helper(new_right_node, new_left_for_right_side, new_right_for_right_side)

    if not arr:
        return None
    if len(arr) == 1:
        root = TreeNode(arr[0])
    else:
        if len(arr)%2 == 0:
            root_val, left_side, right_side = returnEvenVals(arr)
        else:
            root_val, left_side, right_side = returnOddVals(arr)
        root = TreeNode(root_val)
        recursive_helper(root, left_side, right_side)
    return root