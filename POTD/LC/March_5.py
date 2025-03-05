class Solution:
    def coloredCells(self, n: int) -> int:
        return (n*(n+1)-n)+(n*(n-1)-(n-1))
# TC:O(1)
# SC:O(1)
# Approach:Math to compute the total cells