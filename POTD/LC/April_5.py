class Solution:
    def get_subsets(self,arr):
        result = []
        s=0
        def backtrack(index=0, current=[],p_s=0):
            nonlocal s
            if index == len(arr):
                result.append(current[:])
                s+=p_s
                p_s=0
                return
            current.append(arr[index])
            p_s^=arr[index]
            backtrack(index + 1, current,p_s^arr[index])
            current.pop()
            backtrack(index + 1, current,p_s)
        backtrack()
        return s

    def subsetXORSum(self, nums: List[int]) -> int:
        return self.get_subsets(nums)