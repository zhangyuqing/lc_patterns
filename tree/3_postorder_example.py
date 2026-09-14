# LC 543: https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional
from lc_patterns.utils.tree_node import TreeNode

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

            self.tree_diameter = max(
                self.tree_diameter, 
                left_depth + right_depth
            )
            # diameter = # edges, DIFFERENT from depth definition
            # appending to root, # nodes = # edges above each node
            return max(left_depth, right_depth) + 1

        max_depth(root)
        return self.tree_diameter

    def iterative(self, root: Optional[TreeNode]) -> int:
        tree_diameter = 0
        if root is None:
            return tree_diameter

        node_to_depth_map = {}
        # depth = number of nodes along path from node to furthest leaf
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                node_to_depth_map[node] = max(
                    node_to_depth_map.get(node.left, 0),
                    node_to_depth_map.get(node.right, 0)
                ) + 1
                tree_diameter = max(
                    tree_diameter,
                    node_to_depth_map.get(node.left, 0) + node_to_depth_map.get(node.right, 0)
                )
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return tree_diameter
