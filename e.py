'''
ps - https://atcoder.jp/contests/dp/tasks/dp_e
'''

from functools import lru_cache

# @lru_cache(None)
# def helper(idx, v):
#     if v == 0:
#         return 0
#     if idx == n:
#         return float('inf')
    
#     res = helper(idx + 1, v)
#     item_w, item_v = items[idx]
#     if item_v <= v:
#         res = min(res, helper(idx + 1, v - item_v) + item_w)
    
#     return res

def helper(items, n, w):
    dp = [float('inf')] * (max_value + 1)
    dp[0] = 0
    for item_w, item_v in items:
        curr = dp.copy()
        for val in range(item_v, max_value + 1):
            dp[val] = min(dp[val], curr[val - item_v] + item_w)
    return dp

n, w = map(int, input().split())
items = []
max_value = 0
for _ in range(n):
    wi, vi = map(int, input().split())
    items.append((wi, vi))
    max_value += vi

# Find maximum value v such that helper(0, v) <= w
# ans = 0
# for v in range(max_value + 1):
#     if helper(0, v) <= w:
#         ans = v

# print(ans)

dp = helper(items, n, w)
ans = 0
for v in range(max_value + 1):
    if dp[v] <= w:
        ans = v
print(ans)
