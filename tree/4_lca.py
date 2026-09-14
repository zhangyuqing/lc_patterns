# LC 236 https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from tree_node import TreeNode

class LCA:
    def recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            # children pass info whether subtree at children contains p, q, None, or both
            if node is None:
                return None

            if node is p or node is q:
                return node

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            # process node
            if left_result is None:
                return right_result
            elif right_result is None:
                return left_result
            else:
                return node

        return dfs(root)

    def iterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        subtree_results = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                left_res = subtree_results.get(node.left, None)
                right_res = subtree_results.get(node.right, None)
                if p in [left_res, right_res, node] and q in [left_res, right_res, node]:
                    return node
                
                if node is p or node is q:
                    subtree_results[node] = node
                elif left_res is None:
                    subtree_results[node] = right_res
                else:
                    subtree_results[node] = left_res
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
