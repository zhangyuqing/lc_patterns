# LC 210: https://leetcode.com/problems/course-schedule-ii/description/

from collections import deque

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj_list = {i:[] for i in range(numCourses)}
    in_degrees = {i:0 for i in range(numCourses)}

    for p in prerequisites:
        a, b = p[0], p[1]
        adj_list[b].append(a)
        in_degrees[a] += 1

    zero_in_degree_queue = deque([])
    for node, ind in in_degrees.items():
        if ind == 0:
            zero_in_degree_queue.append(node)
    
    output = []
    while zero_in_degree_queue:
        print(zero_in_degree_queue)
        node = zero_in_degree_queue.popleft()
        output.append(node)

        for child in adj_list[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                zero_in_degree_queue.append(child)
    
    if len(output) == numCourses:
        return output
    return []
