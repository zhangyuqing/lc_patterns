# Recursive DFS
# def dfs(node):
#     visited.add(node)
#     for nb in neighbors(node):
#         if nb not in visited:
#             dfs(nb)

# Backtracking
# recursive DFS on state transition tree; state = current partial solution
# def backtrack(state):
#     # process current state
#     if is_answer(state):
#         record_answer(state)
#         return

#     for choice in choices(state):
#         if is_valid(state, choice):
#             make_choice(state, choice) # mutate state in-place
#             backtrack(state)
#             undo_choice(state, choice) # restore state to check the next neighbor/choice

# LC 79: https://leetcode.com/problems/word-search/

def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def backtrack(r, c, curr_len, solution_cells):
        if curr_len == len(word):
            return True

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < m 
                and 0 <= nc < n
                and (nr, nc) not in solution_cells
                and board[nr][nc] == word[curr_len]
            ):
                solution_cells.add((nr, nc))
                if backtrack(nr, nc, curr_len+1, solution_cells):
                    return True
                solution_cells.remove((nr, nc))

        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                curr_solution_cells = set()
                curr_solution_cells.add((i, j))
                if backtrack(i, j, 1, curr_solution_cells):
                    return True
    return False 
