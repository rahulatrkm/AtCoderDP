'''
ps - https://atcoder.jp/contests/dp/tasks/dp_s
Digit DP: Count numbers from 1 to K where digit sum is divisible by D
'''
from functools import lru_cache
import sys
sys.setrecursionlimit(20000)

def helper(k, d):
    digits = [int(x) for x in k]
    n = len(digits)
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(pos, sum_mod, tight, started):
        # Base case: processed all digits
        if pos == n:
            # Valid if digit sum is divisible by D and we've started (not 0)
            return 1 if started and sum_mod == 0 else 0
        
        # Determine digit limit
        limit = digits[pos] if tight else 9
        
        result = 0
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_started = started or (digit > 0)
            new_sum = (sum_mod + digit) % d if new_started else 0
            
            result = (result + dp(pos + 1, new_sum, new_tight, new_started)) % mod
        
        return result
    
    return dp(0, 0, True, False)

k = input()
d = int(input())
print(helper(k, d))
    