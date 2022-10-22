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
    def add(self, current, value):
        arr_length = len(arr)
        midpoint = arr_length // 2

        # set the midpoint to the root of the BST
        self.root = TreeNode(arr[midpoint])

        # set the current to the root
        current = self.root

        # loop from the end of arr until the beginning
        # for index in range(len(arr) - 1, -1, -1):
        for i in arr:
            # if the midpoint is reached, skip it
            # if index == midpoint:
            if i == midpoint:
                continue

            # else if arr[index] is less then the current node...
            # elif arr[index] < current:
            elif i < current:
                # determine if the left subtree is None...
                if current.left is None:
                    # current.left = TreeNode(arr[index])
                    current.left = TreeNode(i)
                else:
                    self.add(current.left, i)
            # if the number is greater than or equal to the current node...
            else:
                # if the current node's right pointer is None...
                if current.right is None:
                    # set the right node to the number
                    current.right = TreeNode(i)
                # otherwise, recurse
                else:
                    self.add(current.right, i)
            
        return self.root   
