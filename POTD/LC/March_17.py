class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        temp={}
        n=len(nums)
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        for i in temp:
            if temp[i]%2:
                return False
        return True
