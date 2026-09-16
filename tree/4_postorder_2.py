# LC 687: https://leetcode.com/problems/longest-univalue-path/description/

from lc_patterns.utils.tree_node import TreeNode
from typing import Optional

class LongestUnivaluePath:
    # subtree pass up: len of lengest path with one end at subtree root
    # CAUTION: len of path = number of edges

    def __init__(self):
        super().__init__()
        self.max_len_unival = 0

    def recursive(self, root: TreeNode | None) -> int:
        
        def dfs(node):
            if node is None:
                return 0
            
            left_res = dfs(node.left) if node.left else 0
            right_res = dfs(node.right) if node.right else 0

            if node.left and node.right and node.val == node.left.val == node.right.val:
                node_res = max(left_res, right_res) + 1
                self.max_len_unival = max(
                    self.max_len_unival,
                    node_res,
                    left_res + right_res + 2
                )
            elif node.left and node.val == node.left.val:
                node_res = left_res + 1
                self.max_len_unival = max(
                    self.max_len_unival,
                    node_res
                )
            elif node.right and node.val == node.right.val:
                node_res = right_res + 1
                self.max_len_unival = max(
                    self.max_len_unival,
                    node_res
                )
            else:
                node_res = 0
            return node_res

        dfs(root)
        return self.max_len_unival 

    def iterative(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        subtree_maxlen = {} # node: max len of univalue path in subtree ending at node
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                left_res = subtree_maxlen.get(node.left, 0)
                right_res = subtree_maxlen.get(node.right, 0)

                if node.left and node.right and node.val == node.left.val == node.right.val:
                    node_res = max(left_res, right_res) + 1
                    self.max_len_unival = max(
                        self.max_len_unival,
                        left_res + right_res + 2
                    )
                elif node.left and node.val == node.left.val:
                    node_res = left_res + 1
                    self.max_len_unival = max(
                        self.max_len_unival,
                        left_res + 1    
                    )
                elif node.right and node.val == node.right.val:
                    node_res = right_res + 1
                    self.max_len_unival = max(
                        self.max_len_unival,
                        right_res + 1    
                    )
                else:
                    node_res = 0

                subtree_maxlen[node] = node_res
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return self.max_len_unival 
