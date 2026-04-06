from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        for s in strs:
            ret[''.join(sorted(s))].append(s)
        return list(ret.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))

strs = ["x"]
print(Solution().groupAnagrams(strs))

strs = [""]
print(Solution().groupAnagrams(strs))