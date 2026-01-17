'''
ps - https://atcoder.jp/contests/dp/tasks/dp_k
'''
from functools import lru_cache
import sys

sys.setrecursionlimit(10**7)


@lru_cache(None)
def helper(k):
    # print(f"helper called with k={k}, player={player}")
    # n = len(moves)
    # m = min(moves)
    # if player == 0:
    #     if k in moves:
    #         return True
    #     if k < m:
    #         return False
    #     for move in moves:
    #         if k - move >= 0 and helper(k - move, 1):
    #             return True
    #     return False
    # else:
    #     if k < m:
    #         return True
    #     for move in moves:
    #         if k - move >= 0 and not helper(k - move, 0):
    #             return False
    #     return True

    # working solution without player parameter
    # if k == 0:
    #     return False

    # for move in moves:
    #     if k - move >= 0 and not helper(k - move):
    #         return True
    # return False

    dp = [False]*(k+1)
    for curr_k in range(1, k+1):
        for move in moves:
            if curr_k - move >= 0 and not dp[curr_k - move]:
                dp[curr_k] = True
                break
    return dp[k]

n, k = map(int, input().split())
moves = list(map(int, input().split()))
if helper(k):
    print("First")
else:
    print("Second")