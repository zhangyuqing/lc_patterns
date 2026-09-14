# LC 295: https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self.large) == 0:
            heappush(self.large, num)
        elif num >= self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)

        while len(self.large) > len(self.small) + 1:
            num = heappop(self.large)
            heappush(self.small, -num)
        while len(self.small) > len(self.large):
            num = heappop(self.small)
            heappush(self.large, -num)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.
        else:
            return float(self.large[0])
