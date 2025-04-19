class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def pairs( val:int )->int :
            res=0
            j=len(nums)-1
            for i in range(len(nums)):
                while i<j and nums[i]+nums[j]>val:
                    j-=1
                res+=(max(0,j-i))
            return res
        nums.sort()
        return pairs(upper)-pairs(lower-1)
