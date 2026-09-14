from tree_node import TreeNode
from typing import Optional, List
from collections import deque
# deque: array that can popleft()

class BFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = deque([root])

        while q:
            level_size = len(q) # fix level size each level
            curr_level = []
            for i in range(level_size):
                node = q.popleft()
                if node:
                   curr_level.append(node.val)
                   q.append(node.left)
                   q.append(node.right)
            if curr_level:
                output.append(curr_level)

        # or alternatively, only put non empty node in queue
        return output
