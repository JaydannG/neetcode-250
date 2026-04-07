from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = defaultdict(int)
        for num in nums:
            l[num] += 1

        sorted_l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
        ret = []
        for i in range(k):
            ret.append(list(sorted_l)[i])
        return ret