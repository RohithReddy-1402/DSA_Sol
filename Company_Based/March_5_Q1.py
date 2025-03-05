# https://leetcode.com/problems/reconstruct-original-digits-from-english/
class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter

        char_count = Counter(s)
        nums_count = [0] * 10
        nums_count[0] = char_count['z']  
        nums_count[2] = char_count['w'] 
        nums_count[4] = char_count['u']
        nums_count[6] = char_count['x']  
        nums_count[8] = char_count['g']  
        nums_count[3] = char_count['h'] - nums_count[8]  
        nums_count[5] = char_count['f'] - nums_count[4]  
        nums_count[7] = char_count['s'] - nums_count[6]  
        nums_count[1] = char_count['o'] - (nums_count[0] + nums_count[2] + nums_count[4])  
        nums_count[9] = char_count['i'] - (nums_count[5] + nums_count[6] + nums_count[8]) 

        return "".join(str(i) * nums_count[i] for i in range(10))
# TC:O(N)
# SC:O(N)
# Approach: make the dict of char of string and find the digits based on characters in the original names of digits