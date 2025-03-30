class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen={}
        for i in range(len(s)):
            last_seen[s[i]]=i
        max_last_seen=-1
        res=[]
        prev_seen=-1
        for i in range(len(s)):
            max_last_seen=max(max_last_seen,last_seen[s[i]])
            if i==max_last_seen:
                
                res.append(max_last_seen-prev_seen)
                prev_seen=max_last_seen
                max_last_seen=0
        return res