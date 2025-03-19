class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        min_req=0
        n=len(nums)
        for i in range(n-2):
            if nums[i]==0:
                for x in range(i,i+3):
                    nums[x]=nums[x]^1
                min_req+=1
        if not sum(nums)==n:
            return -1
        return min_req
# TC : O(N)
# SC : O(1)
# Approach : itterate through the array and toogle the ele if zero and verify by sum