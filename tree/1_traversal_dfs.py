from tree_node import TreeNode
from typing import Optional, List


class DFSRecursive:
    def traversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(node):
            if node is None:
                return 

            # pre
            output.append(node.val)
            dfs(node.left)
            dfs(node.right)
            # in: left => node => right
            # post: left => right => node

        dfs(root)
        return output


class DFSIterative:
    def traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        output = []
        stack = [(root, False)] # node, visited
        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    output.append(node.val)
                else:
                    # reverse of recursion order
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
                    # in: right => node => left
                    # post: node => right => left

        return output
