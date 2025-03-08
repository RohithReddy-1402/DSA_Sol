class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_count=-1
        temp=0
        for i in blocks[:k]:
            if i=='W':
                temp+=1
        ans,l=temp,0
        for i in range(k,len(blocks)):
            if blocks[l]=='W':
                temp-=1
            l+=1
            if blocks[i]=='W':
                temp+=1
            ans=min(ans,temp)
        return ans
# TC:(K*(N-k+1))
# SC:O(1)
# Approach:loop through the string and find the min of toggles required.