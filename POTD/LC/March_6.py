class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res=[]
        n=len(grid)
        for i in range(n):
            for j in range(n):
                num=abs(grid[i][j])-1
                row,col=num//n,num % n
                if grid[row][col]<0 :
                    res.append(num+1)
                else:
                    grid[row][col]=-grid[row][col]
        for i in range(n):
            for j in range(n):
                if grid[i][j]>0:
                    res.append(i*n+j+1)
                    break
        return res
# TC:O(N^2)
# SC:O(1)
# Approach: first go through the grid and mark the visited elements as negative , by that we can find the repeated number and element which is +ve by that we can find the missing number