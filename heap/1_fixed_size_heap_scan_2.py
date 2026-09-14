# LC 692: https://leetcode.com/problems/top-k-frequent-words/description/
from typing import List
from collections import Counter
from heapq import heappush, heappop

def topKFrequent(words: List[str], k: int) -> List[str]:
    # build frequency map
    freq_map = Counter(words)

    # usually, largest => min heap, smallest => max heap
    # but this question needs large freqeuncy comes first, small word comes first
    # easier to manipulate order of frequency => use max heap then pop K times

    h = []
    for word, freq in freq_map.items():
        heappush(h, (-freq, word))

    output = []
    for _ in range(k):
        _, word = heappop(h)
        output.append(word)
    return output


