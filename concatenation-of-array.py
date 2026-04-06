from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums) * 2
        for i, num in enumerate(nums):
            ret[i] = ret[i + len(nums)] = num
        
        return ret

nums = [1, 4, 1, 2]
print(Solution().getConcatenation(nums))

nums = [22, 21, 20, 1]
print(Solution().getConcatenation(nums))