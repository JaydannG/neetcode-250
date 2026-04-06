from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = [x for x in nums if x != val]
        nums[:] = tmp
        return len(nums)

nums = [1,1,2,3,4], val = 1
print(Solution().removeElement(nums, val), nums)

nums = [0,1,2,2,3,0,4,2], val = 2
print(Solution().removeElement(nums, val), nums)