'''
ps - https://atcoder.jp/contests/dp/tasks/dp_y
'''
import sys
input = sys.stdin.readline

def solve():
    MOD = 10**9 + 7
    h, w, n = map(int, input().split())
    
    MAX = h + w + 1
    fact = [1] * MAX
    for i in range(1, MAX):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact = [1] * MAX
    inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
    for i in range(MAX - 2, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
    
    def paths(r1, c1, r2, c2):
        dr, dc = r2 - r1, c2 - c1
        if dr < 0 or dc < 0:
            return 0
        return nCr(dr + dc, dr)
    
    walls = []
    for _ in range(n):
        r, c = map(int, input().split())
        walls.append((r, c))
    walls.append((h, w))
    walls.sort()
    
    m = len(walls)
    dp = [0] * m
    
    for i in range(m):
        r, c = walls[i]
        dp[i] = paths(1, 1, r, c)
        for j in range(i):
            rj, cj = walls[j]
            if rj <= r and cj <= c:
                dp[i] = (dp[i] - dp[j] * paths(rj, cj, r, c)) % MOD
    
    print(dp[-1] % MOD)

solve()