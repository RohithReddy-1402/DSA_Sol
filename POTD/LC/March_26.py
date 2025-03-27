
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        total_count = nums.count(candidate)
        if total_count * 2 <= len(nums):  
            return -1
        prefix_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                prefix_count += 1
            if prefix_count * 2 > (i + 1) and (total_count - prefix_count) * 2 > (len(nums) - (i + 1)):
                return i
        
        return -1

# TC : O( N )
# SC : O( 1 )
# Approach : using the Boyer-Moore algo find the major element and check for the smallest index