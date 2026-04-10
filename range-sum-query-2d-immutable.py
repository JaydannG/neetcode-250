from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = 0
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                ret += self.data[row][col]

        return ret