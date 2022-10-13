class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

# arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    def build(start, end):
            if start > end: 
                return 
            
            mid_index = (start+end)//2
            root = TreeNode(arr[mid_index])
            
            root.left = build(start, mid_index - 1)
            root.right = build(mid_index + 1, end)
            
            return root
    
    return build(0, len(arr)-1)
