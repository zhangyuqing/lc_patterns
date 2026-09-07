from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSRecursive:
    def orderedTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
