'''
ps - https://atcoder.jp/contests/dp/tasks/dp_t
'''

def solve():
    MOD = 10**9 + 7
    n = int(input())
    s = input().strip()
    
    dp = [[0] * (n + 2) for _ in range(2)]
    dp[1][1] = 1
    
    for i in range(2, n + 1):
        curr = i % 2
        prev = (i - 1) % 2
        
        for j in range(n + 2):
            dp[curr][j] = 0
        
        prefix = [0] * (n + 2)
        for j in range(1, i):
            prefix[j] = (prefix[j - 1] + dp[prev][j]) % MOD
        
        for j in range(1, i + 1):
            if s[i - 2] == '<':
                if j > 1:
                    dp[curr][j] = prefix[j - 1]
            else:
                dp[curr][j] = (prefix[i - 1] - prefix[j - 1] + MOD) % MOD
    
    ans = 0
    last = n % 2
    for j in range(1, n + 1):
        ans = (ans + dp[last][j]) % MOD
    print(ans)

solve()