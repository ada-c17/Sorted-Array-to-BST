class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right



# class Tree:
#     def __init__(self):
#         self.root = None

#     def add_helper(self, current_node, new_node):
#         if new_node.val < current_node.val:
#             if not current_node.left:
#                 current_node.left = new_node
#                 return
#             else:
#                 self.add_helper(current_node.left, new_node)
#         elif new_node.val >= current_node.val:
#             if not current_node.right:
#                 current_node.right = new_node
#                 return
#             else:
#                 self.add_helper(current_node.right, new_node)

#     def add(self, val):
#         new_node = TreeNode(val)
#         if not self.root:
#             self.root = new_node
#         else:
#             self.add_helper(self.root, new_node)

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if not arr:
        return None
    elif len(arr) == 1:
        return TreeNode(arr[0])
    else:
        if len(arr)% 2 == 0:
            median_index = int(len(arr)/2)
            median = arr[median_index]
        else:
            median_index = int((len(arr)-1)/2)
            median = arr[median_index]
        arr_left = arr[0:median_index]
        arr_right = arr[median_index+1:]
        median_node = TreeNode(median)
        median_node.left = arr_to_bst(arr_left)
        median_node.right = arr_to_bst(arr_right)
        return median_node
