# LC 684: https://leetcode.com/problems/redundant-connection/

## Traversal
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    for i in range(n-1, -1, -1):
        edge_to_remove = edges[i]

        # build graph without the edge
        adj_list = {x: [] for x in range(1, n+1)}
        for j in range(n):
            if j != i:
                e = edges[j]
                adj_list[e[0]].append(e[1])
                adj_list[e[1]].append(e[0])

        # traverse graph
        visited = set()
        frontier = [1]
        while frontier:
            node = frontier.pop()
            if node not in visited:
                visited.add(node)

                for nb in adj_list[node]:
                    frontier.append(nb)

        if len(visited) == n:
            return edge_to_remove


## Union Find
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)

    cc = [i for i in range(n+1)]
    # root of i at index i, 0 - no use

    def find(x):
        if cc[x] != x:
            cc[x] = find(cc[x])
        return cc[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        cc[rb] = ra
        return True

    for e in edges:
        if not union(e[0], e[1]):
            return e

