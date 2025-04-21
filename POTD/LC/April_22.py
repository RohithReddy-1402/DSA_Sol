class Solution:
    def numberOfArrays(self, d: List[int], lower: int, upper: int) -> int:
        num = 0
        maxVal, minVal = 0, 0
        for delta in d:
            num += delta
            maxVal = max(maxVal, num)
            minVal = min(minVal, num)
        return max(0, (upper - lower) - (maxVal - minVal) + 1)
