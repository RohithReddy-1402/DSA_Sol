class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_count=-1
        temp=0
        for i in blocks:
            if i=='B':
                temp+=1
            else:
                max_count=max(max_count,temp)
                temp=0
        if max_count>=k:
            return 0
        else:
            min_toggle=float('inf')
            for i in range(len(blocks)-k+1):
                temp=0
                for j in range(i,i+k):
                    if not blocks[j]=='B':
                        temp+=1
                min_toggle=min(min_toggle,temp)
            return min_toggle
# TC:(K*(N-k+1))
# SC:O(1)
# Approach:loop through the string and find the min of toggles required.