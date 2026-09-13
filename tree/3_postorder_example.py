# LC 543: https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional
from tree_node import TreeNode

class DiameterOfBinaryTree:
    def __init__(self):    
        self.tree_diameter = 0

    def recursive(self, root: Optional[TreeNode]) -> int:

        def max_depth(node):
            # return # node along longest path of subtree at node
            if node is None:
                return 0

            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)

            self.tree_diameter = max(self.tree_diameter, left_depth + right_depth)
            # diameter = # edges
            # appending to root, # nodes = # edges above each node
            return max(left_depth, right_depth) + 1

        max_depth(root)
        return self.tree_diameter

    def iterative(self, root: Optional[TreeNode]) -> int:
        pass