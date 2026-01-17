'''
ps - https://atcoder.jp/contests/dp/tasks/dp_x
'''
import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)

n = int(input())
blocks = [tuple(map(int, input().split())) for _ in range(n)]

# Sort by weight + solidity (critical for correctness)
blocks.sort(key=lambda x: x[0] + x[1])

@lru_cache(maxsize=None)
def dp(i, weight_above):
    """Max value using blocks[i:] with weight_above already on top."""
    if i == n:
        return 0
    
    w, s, v = blocks[i]
    
    # Option 1: Skip this block
    ans = dp(i + 1, weight_above)
    
    # Option 2: Use this block (only if it can support weight_above)
    if weight_above <= s:
        ans = max(ans, dp(i + 1, weight_above + w) + v)
    
    return ans

print(dp(0, 0))


# ==================== TABULAR DP SOLUTION ====================
# max_weight = sum(b[0] for b in blocks)
# dp = [0] * (max_weight + 1)
#
# for w, s, v in blocks:
#     # Process in reverse to avoid using same block twice
#     # Can place this block if current weight <= solidity
#     for curr_w in range(min(s, max_weight - w), -1, -1):
#         dp[curr_w + w] = max(dp[curr_w + w], dp[curr_w] + v)
#
# print(max(dp))


# ==================== ORIGINAL BRUTE FORCE SOLUTION ====================
# (Too slow for large inputs - O(n!) complexity)
#
# n = int(input())
# # wt, sol, val
# blocks = []
# for _ in range(n):
#     blocks.append(tuple(map(int, input().split())))
#
# # blocks.sort(key=lambda x: (x[1], -x[0], x[2]), reverse=True)
# # print(blocks)
#
# vis = set()
# def helper(sol):
#     # print(f"sol: {sol}, vis: {vis}")
#     if sol < 0:
#         return -float('inf')
#     
#     if len(vis) == n:
#         return 0
#     ans = 0
#     for i in range(n):
#         if i not in vis and blocks[i][0] <= sol:
#             vis.add(i)
#             ans = max(ans, helper(min(sol - blocks[i][0], blocks[i][1])) + blocks[i][2])
#             vis.remove(i)
#     return ans
#
# print(helper(float('inf')))