from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        ret = ""
        for word in strs:
            sizes.append(len(word))

        for sz in sizes:
            ret += str(sz)
            ret += ","
    
        ret += "#"

        for word in strs:
            ret += word

        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        sizes = []
        ret = []

        while s[i] != "#":
            curr = ""
            while s[i] != ',':
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1

        for sz in sizes:
            ret.append(s[i:i + sz])
            i += sz

        return ret

print(Solution().encode(["Hello", "World"]))
print(Solution().decode("5,5,#HelloWorld"))