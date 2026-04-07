from typing import List

class Solution:
    def mergesort(self, data, left, right):
        if left < right:
            mid = (left + right) // 2

            self.mergesort(data, left, mid)
            self.mergesort(data, mid + 1, right)
            self.merge(data, left, mid, right)

    def merge(self, data, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = data[left + i]
        for i in range(n2):
            R[i] = data[mid + i + 1]

        i = j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            data[k] = L[i]
            i += 1
            k += 1 

        while j < n2:
            data[k] = R[j]
            j += 1
            k += 1
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums
        