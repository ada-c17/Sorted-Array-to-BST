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
    if arr is None or len(arr) == 0:
        return None

    # find middle index of the sorted array
    mid_array_index = (len(arr)) // 2
     
    # make the middle element the root
    root = TreeNode(arr[mid_array_index])
     
    # left subtree of root has all values less than mid of arr
    root.left = arr_to_bst(arr[:mid_array_index])
     
    # left subtree of root has all values > than mid of arr
    root.right = arr_to_bst(arr[mid_array_index+1:])
    return root 

def printTree(node):
    if node == None:
        return
    printTree(node.left)
    print(node.val) 
    printTree(node.right)

    
arr=[1,2,3,4,5,6,7,8]

root_node = arr_to_bst(arr)
print(root_node .val)
