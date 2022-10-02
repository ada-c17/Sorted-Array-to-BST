from __future__ import annotations
from typing import Any, List, Optional

class TreeNode:
    def __init__(self, value: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> TreeNode:
        self.val = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, sorted_values: List[Any]) -> Tree:
        self.root = self.new_subtree_root(sorted_values)

    def new_subtree_root(self, sorted_arr: List[Any]) -> Optional[TreeNode]:
        if not sorted_arr:
            return None
        i = len(sorted_arr) // 2
        return TreeNode(
            sorted_arr[i], 
            self.new_subtree_root(sorted_arr[:i]), 
            self.new_subtree_root(sorted_arr[i+1:])
        )


def arr_to_bst(arr) -> TreeNode:
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    return Tree(arr).root