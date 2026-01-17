'''
ps - https://atcoder.jp/contests/dp/tasks/dp_s
'''

def solve():
    MOD = 10**9 + 7
    k = input().strip()
    d = int(input())
    
    digits = [int(x) for x in k]
    n = len(digits)
    
    dp = [[[0] * 2 for _ in range(d)] for _ in range(n + 1)]
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
                    dp[pos + 1][new_sum][new_tight] = (dp[pos + 1][new_sum][new_tight] + dp[pos][sum_mod][tight]) % MOD
    
    ans = (dp[n][0][0] + dp[n][0][1] - 1) % MOD
    print(ans)

solve()