'''
ps - https://atcoder.jp/contests/dp/tasks/dp_s
'''

import sys
sys.setrecursionlimit(20000)

k = input()
d = int(input())
mod = 10**9+7

# Iterative DP (faster)
digits = [int(x) for x in k]
n = len(digits)

# dp[pos][sum_mod][tight] = count of valid numbers
dp = [[[0]*2 for _ in range(d)] for _ in range(n+1)]
dp[0][0][1] = 1

for pos in range(n):
    for sum_mod in range(d):
        for tight in range(2):
            if dp[pos][sum_mod][tight] == 0:
                continue
            
            limit = digits[pos] if tight else 9
            
            for digit in range(limit + 1):
                new_sum = (sum_mod + digit) % d
                new_tight = 1 if (tight and digit == limit) else 0
                dp[pos+1][new_sum][new_tight] = (dp[pos+1][new_sum][new_tight] + dp[pos][sum_mod][tight]) % mod

# Sum all combinations where sum_mod == 0, subtract 1 for zero
ans = (dp[n][0][0] + dp[n][0][1] - 1) % mod
print(ans)

# Recursive version (kept for reference, commented out)
# memo = {}
# def helper(pos, sum_mod, tight):
#   global k, d, mod, memo
#   if (pos, sum_mod, tight) in memo:
#     return memo[(pos, sum_mod, tight)]
#   
#   if pos == len(k):
#     return 1 if sum_mod%d == 0 else 0
#   
#   limit = int(k[pos]) if tight else 9
#   ans = 0
#   for i in range(limit+1):
#     ans = (ans + helper(pos+1, (sum_mod+i)%d, tight and i==limit)) % mod
#   memo[(pos, sum_mod, tight)] = ans
#   return ans
# print((helper(0, 0, True)-1)%mod)