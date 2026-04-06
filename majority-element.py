from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = defaultdict(int)

        for num in nums:
            l[num] += 1

            if l[num] > len(nums) // 2:
                return num


nums = [2,2,2]
print(Solution().majorityElement(nums))

nums = [5,5,1,1,1,5,5]
print(Solution().majorityElement(nums))