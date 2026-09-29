# LC 797: https://leetcode.com/problems/all-paths-from-source-to-target/

def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    N = len(graph)
    output = []

    def backtrack(curr_node, curr_path):
        if curr_node == N-1:
            output.append(curr_path.copy())
            return

        for nb in graph[curr_node]:
            curr_path.append(nb)
            backtrack(nb, curr_path)
            curr_path.pop()
    
    backtrack(0, [0])
    return output
