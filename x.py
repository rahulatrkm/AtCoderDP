'''
ps - https://atcoder.jp/contests/dp/tasks/dp_x
'''
import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)

def solve():
    n = int(input())
    blocks = [tuple(map(int, input().split())) for _ in range(n)]
    blocks.sort(key=lambda x: x[0] + x[1])
    
    @lru_cache(maxsize=None)
    def dp(i, weight_above):
        if i == n:
            return 0
        w, s, v = blocks[i]
        ans = dp(i + 1, weight_above)
        if weight_above <= s:
            ans = max(ans, dp(i + 1, weight_above + w) + v)
        return ans
    
    print(dp(0, 0))

solve()