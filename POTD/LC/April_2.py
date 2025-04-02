class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mx=max(nums[0],nums[1])
        d=nums[0]-nums[1]
        res=0
        for i in range(2,len(nums)):
            v=nums[i]
            res=max(res,d*v)
            mx=max(mx,v)
            d=max(d,mx-v)
        return res
        