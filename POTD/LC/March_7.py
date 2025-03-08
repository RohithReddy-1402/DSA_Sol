    def prime(n):
        if n<=1:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        else:
            for i in range(3,int(n**(0.5))+1,2):
                if n%i==0:
                    return False
            return True
    class Solution:
        def closestPrimes(self, left: int, right: int) -> List[int]:
            num1,num2=-1,-1
            temp1,temp2=-1,-1
            diff=float('inf')
            for i in range(left,right+1):
                if(prime(i)):
                    temp2=temp1
                    temp1=i
                    
                    if temp1-temp2<diff:
                        diff=temp1-temp2
                        num1=temp2
                        num2=temp1
                        if diff==2:
                            return [num1,num2]
            return [num1,num2] if num1>0 and num2>0 else [-1,-1]
    # TC:O(m(right)^(0.5))
    # SC:O(1)
    # Approach:Loop from left to right and find the pair for the closest by calculating .