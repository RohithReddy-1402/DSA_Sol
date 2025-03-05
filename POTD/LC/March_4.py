class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            while not n % 3:
                n //= 3
            
            if n % 3 == 2:
                return False
            n -= n % 3
        return True
# TC:log(N)/Log(3)
# SC:O(1)
# Approach:Divide the number if it divisable by 3 and return false it returns 2 as remainder