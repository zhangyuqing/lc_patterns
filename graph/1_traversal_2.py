# LC 542: https://leetcode.com/problems/01-matrix/

from collections import deque

def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])

    # find 1s that are neighbor to 0s
    frontier = deque([])
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                neighbor_to_0 = False
                for di, dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                    ni, nj = i + di, j+dj
                    if (
                        0 <= ni < m
                        and 0 <= nj < n
                        and mat[ni][nj] == 0
                    ):
                        neighbor_to_0 = True
                
                if neighbor_to_0:
                    frontier.append((i, j, 1))

    # BFS with value to fill in the cells
    visited = set()
    while frontier:
        r, c, d = frontier.popleft()

        if (r, c) not in visited:
            visited.add((r, c))

            mat[r][c] = d

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                    and mat[nr][nc] != 0
                ):
                    frontier.append((nr, nc, d+1))

    return mat
