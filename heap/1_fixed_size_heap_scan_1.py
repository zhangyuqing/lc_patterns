# LC 973: https://leetcode.com/problems/k-closest-points-to-origin/description/

from typing import List
from heapq import heappush, heappop

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # K smallest => max heap
    h = []
    for p in points:
        x, y = p[0], p[1]
        dist_sq = x ** 2 + y ** 2
        heappush(h, (-dist_sq, x, y))
        if len(h) > k:
            heappop(h)

    output = [[item[1], item[2]] for item in h]
    return output
