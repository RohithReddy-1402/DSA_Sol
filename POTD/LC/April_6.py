class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > dp[max_index]:
                max_index = i
        result = []
        i = max_index
        while i >= 0:
            result.append(nums[i])
            i = prev[i]
        return result[::-1] 
# TC: O(n^2)
# SC: O(n)
# Approach: Sort the array and use dp by storing the largest and previous index of the largest divisible subset