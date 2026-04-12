from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ret = []
        for num in c:
            if c[num] > len(nums) // 3:
                ret.append(num)

        return ret