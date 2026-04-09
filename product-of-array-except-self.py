from typing import List
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(int(math.prod(nums[:i]) * math.prod(nums[i + 1:])))

        return ret