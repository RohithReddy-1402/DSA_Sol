class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, OR, max_len = 0, 0, 0

        for r in range(len(nums)):
            while (OR & nums[r]) != 0:
                OR ^= nums[l]
                l += 1  
            OR |= nums[r]  
            max_len = max(max_len, r - l + 1)
        
        return max_len
# TC :O(n)
# SC :O(1)
# Approach :
