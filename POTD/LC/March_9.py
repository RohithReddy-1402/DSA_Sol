class Solution:
    def numberOfAlternatingGroups(self, arr: List[int], k: int) -> int:
        n = len(arr) 
        temp = sum(arr[i] ^ arr[i + 1] for i in range(k - 1))
        alter = 1 if temp == k - 1 else 0
        for i in range(1, n):
            temp -= arr[i - 1] ^ arr[i]  
            temp += arr[(i + k - 2) % n] ^ arr[(i + k - 1) % n]  

            if temp == k - 1:
                alter += 1
        return alter
# TC:O(N)
# SC:O(1)
# Approach: find the the sum of xor of first k elements and then use sliding window .
#  