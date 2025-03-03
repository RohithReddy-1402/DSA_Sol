class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        i = 0
        j = 0

        for k in range(n):
            if nums[k] < pivot:
                nums.insert(i, nums.pop(k))
                i += 1
        j = i  
        for k in range(i, n):
            if nums[k] == pivot:
                nums.insert(j, nums.pop(k)) 
                j += 1

        return nums
# TC:O(N)
# SC:O(1)
# Approach: using two pointers first swap the insert the elements which are less than pivot and then insert the elements which are greater than pivot after pivot