'''
ps - https://atcoder.jp/contests/dp/tasks/dp_y
'''
import sys
input = sys.stdin.readline

def solve():
    MOD = 10**9 + 7
    h, w, n = map(int, input().split())
    
    # Precompute factorials and inverse factorials for nCr
    MAX = h + w + 1
    fact = [1] * MAX
    for i in range(1, MAX):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * MAX
    inv_fact[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
    for i in range(MAX-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD
    
    def paths(r1, c1, r2, c2):
        """Number of paths from (r1,c1) to (r2,c2) moving only right/down"""
        dr, dc = r2 - r1, c2 - c1
        if dr < 0 or dc < 0:
            return 0
        return nCr(dr + dc, dr)
    
    # Read walls and add destination as a "wall" for uniform processing
    walls = []
    for _ in range(n):
        r, c = map(int, input().split())
        walls.append((r, c))
    walls.append((h, w))  # Add destination
    
    # Sort walls by row, then by column (to process in order)
    walls.sort()
    
    # dp[i] = number of valid paths from (1,1) to walls[i] (not passing through any earlier wall)
    m = len(walls)
    dp = [0] * m
    
    for i in range(m):
        r, c = walls[i]
        # Total paths from (1,1) to (r,c)
        dp[i] = paths(1, 1, r, c)
        # Subtract paths that go through an earlier wall
        for j in range(i):
            rj, cj = walls[j]
            if rj <= r and cj <= c:
                # Subtract paths that pass through wall j
                dp[i] = (dp[i] - dp[j] * paths(rj, cj, r, c)) % MOD
    
    print(dp[-1] % MOD)

solve()