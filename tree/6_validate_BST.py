# LC 98: https://leetcode.com/problems/validate-binary-search-tree/description/

from lc_patterns.utils.tree_node import TreeNode

def isValidBST(root: TreeNode | None) -> bool:
        
    def dfs(node, lb, ub):
        # ok to do pre-order traversal
        # node.val must be within (lb, ub) - exclusive
        if node is None:
            return True
        
        if node.val <= lb or node.val >= ub:
            return False
        
        left_res = dfs(node.left, lb, min(ub, node.val))
        right_res = dfs(node.right, max(lb, node.val), ub)
        return left_res and right_res

    return dfs(root, float('-inf'), float('inf'))
