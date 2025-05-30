# Question : https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict) 
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  

        for i in range(1, n + 1):  
            for j in range(i):  
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  

        return dp[n]  
# TC : O(N^2)
#  SC : O(n+m*k)
#  Approach : using dp check whether substring is present in the wordlist