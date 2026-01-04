'''
ps - https://atcoder.jp/contests/dp/tasks/dp_e
'''

from functools import lru_cache


@lru_cache(None)
def helper(idx, w):
    if idx == len(wv):
        return 0
    item_w, item_v = wv[idx]
    if item_w <= w:
        return max(helper(idx + 1, w), helper(idx + 1, w - item_w) + item_v)
    return helper(idx + 1, w)

n, w = map(int, input().split())
wv = []
for _ in range(n):
    wv.append(tuple(map(int, input().split())))

print(helper(0, w))