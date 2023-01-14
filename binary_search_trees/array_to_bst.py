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

    class BinarySearch_tree:
        def __init__(self) :
            self.root   = None  

        def insert(self, value):
#      check for duplicates
            if  value ==  self.root.value:
                return 
    #      If root is empty
            mid_point  = len(arr)//2
            if self.root == None:
                self.root =  TreeNode(arr[mid_point])
            else:
                self.insertNode(value, self.root)

# recursive function
        def insertNode(self, value, current_node):
            if value < current_node.value:
                if current_node.left == None:
                     current_node.left == TreeNode(value)                    
#                       else set left to current_node
                else:
                    self.insertNode(value, current_node.left) 
#           else check the right side
            else:
                if current_node.right == None:
                    current_node.right = TreeNode(value)
                else: 
                    self.insertNode(value, current_node.right) 
           


        def  printFunc(self, current_node):     
            if self.root !=None:
             self.printTree(self.root)

        def printTree( self, current_node):
            if current_node !=None:
                self.printTree(current_node.left) 
                print ( str(current_node.value))
                self.printTree(current_node.rightt)       








    # arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    # Finding the midpoint
# Step one -find mid-point in  sorted arrray
#  assign mid-point to root
# find length and integer diviide by 2 
#  if the %  of length  
    #   mid-point == len(arr)//2
    
    # if len(arr)%2 == 0:
         #  x = len(arr) //2    
    # else  
    # y = len(arr) 

    # Duplicate values check
    # compare value being passed in to value in current node. If equals the value in current node, return

    # if tree is empty assign value to root