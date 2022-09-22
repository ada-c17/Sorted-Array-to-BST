class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

    def add(self, current, i):     
        if self.val < current.val:
            if not current.left:
                current.left = self
                print(f'New Left: {current.left.val}')
            current = current.left
            print(f'New Current: {current.val}')
        else:
            if not current.right:
                current.right = self
                print(f'Right: {current.right.val}')
            current = current.right

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    if not arr:
        return None
    else:
        mid = len(arr)//2 
        middle = arr[mid]   
        root = TreeNode(middle)
        current = root
    
        i = 0
        while i >= len(arr):
            t = TreeNode(arr[i])
            t.add(current, i)
            i += 1
        
        return root

# arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]

# # Act
# answer = arr_to_bst(arr)
# print(answer.val) # 25