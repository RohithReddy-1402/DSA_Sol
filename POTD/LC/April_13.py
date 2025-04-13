class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        primes = n // 2
        evens = n - primes
        return (pow(5, evens, MOD) * pow(4, primes, MOD)) % MOD   