# LC 23: https://leetcode.com/problems/merge-k-sorted-lists/description/

from lc_patterns.utils.list_node import ListNode
from typing import List, Optional
from heapq import heappush, heappop


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
        return None

    h = []
    for i in range(len(lists)):
        if lists[i]:
            heappush(h, (lists[i].val, i))
    if len(h) == 0:
        return None

    _, root_idx = heappop(h)
    root = lists[root_idx]
    lists[root_idx] = lists[root_idx].next
    if lists[root_idx]:
        heappush(h, (lists[root_idx].val, root_idx))

    p = root
    while h:
        _, idx = heappop(h)
        p.next = lists[idx]
        p = p.next
        lists[idx] = lists[idx].next
        if lists[idx]:
            heappush(h, (lists[idx].val, idx))
    return root
