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
    first = 0
    last = len(arr)-1
    def mid_helper(first, last):
        if first > last:
            return None
        mid= (first + last) //2
        root = TreeNode(arr[mid])
        root.left= mid_helper(first,mid-1)
        root.right=mid_helper(mid+1,last)
        print(root.val)
        return root

    return mid_helper(first, last)
    