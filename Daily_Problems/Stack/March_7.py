# https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
class Solution:
    def calculateSpan(self, arr):
        #write code here
        res=[1]
        n=len(arr)
        check_list=[[arr[0],0]]
        for i in range(1,n):
            while check_list and check_list[-1][0]<=arr[i]:
                check_list.pop()
            if not check_list:
                res.append(i+1)
            else :
                res.append(i-check_list[-1][1])
            check_list.append([arr[i],i])
        return res
# TC:O(n)
# SC:O(N)
