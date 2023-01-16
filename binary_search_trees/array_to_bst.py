class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right



def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.


        `arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]`

                        25 
                     /      \
                    15        35
                   / \        / \
                 10   20     30  40
                /                  \
               5                    45
    """
    if not arr: 
        return None 
    mid = len(arr)//2 
    # find midpoint each time the function is recursively called 
    current_node = TreeNode(arr[mid])
    # grab left side of mid 
    #  recursively call function to find mid of left side 
    current_node.left = arr_to_bst(arr[:mid])
    # grab right side of mid, skip mid, recursively call to find mid of right side 
    current_node.right = arr_to_bst(arr[mid + 1:])

    return current_node 



# # create helper function to print result 
# def preOrderNodes(current_node): 
#     if not current_node: 
#         return 
#     print(current_node.val)
#     preOrderNodes(current_node.left)
#     preOrderNodes(current_node.right)


# arr = arr_to_bst([5, 10, 15, 20, 25, 30, 35, 40, 45])
# preOrderNodes(arr)



    
    



