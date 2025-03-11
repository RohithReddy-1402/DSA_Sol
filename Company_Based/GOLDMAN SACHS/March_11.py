class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_num = max(nums)

        dp = [0] * (max_num + 1)
        
        for num in range(max_num + 1):
            dp[num] = freq[num] * num

        prev, curr = 0, 0
        for i in range(max_num + 1):
            prev, curr = curr, max(curr, prev + freq[i]*i)

        return curr
# TC:O(N+M
# SC:O(1)
# Approach : using dp , find the max points by skipping consective steps and finding the max