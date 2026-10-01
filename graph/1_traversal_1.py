# Iterative DFS & BFS template
# - pop
# - check & add visited
# - process node
# - expand & push
# 
# def search(start):
#     visited = set()
#     frontier = [(start, other info...)]     # queue for BFS, stack for DFS
# 
#     while frontier:
#         node = frontier.pop(...)
#         if node not in visited:
#             visited.add(node)
#             
#             # process node
#
#             for nb in neighbors(node):
#                 frontier.push(nb)

# Recursive DFS
# def dfs(node):
#     visited.add(node)
#     for nb in neighbors(node):
#         if nb not in visited:
#             dfs(nb)

# LC 841: https://leetcode.com/problems/keys-and-rooms/description/
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    # build directed graph
    n = len(rooms)
    graph = {i:rooms[i] for i in range(n)}
    # u: [v] - there's a directed edge from u to v

    visited = set()
    frontier = [0]
    while frontier:
        node = frontier.pop()

        if node not in visited:
            visited.add(node)

            for nb in graph[node]:
                frontier.append(nb)
    
    if len(visited) == n:
        return True
    return False
