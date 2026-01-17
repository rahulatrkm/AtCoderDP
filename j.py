'''
ps - https://atcoder.jp/contests/dp/tasks/dp_j
'''

from functools import lru_cache


# @lru_cache(None)
def helper(curr):
    # if sum(curr) == 0:
    #     return 0
    # curr = list(curr)
    # ans = 0
    # n = len(curr)
    # cnt = n - curr.count(0)
    # for i in range(n):
    #     if curr[i] > 0:
    #         curr[i] -= 1
    #         ans += helper(tuple(curr))
    #         curr[i] += 1
    # return ans/cnt + n/cnt

    # @lru_cache(None)
    # def dp_helper(c1, c2, c3, n):
    #     if c1 == 0 and c2 == 0 and c3 == 0:
    #         return 0.0
    #     ans = 0.0
    #     total = c1 + c2 + c3
    #     if c1 > 0:
    #         ans += dp_helper(c1 - 1, c2, c3, n)*c1
    #     if c2 > 0:
    #         ans += dp_helper(c1 + 1, c2 - 1, c3, n)*c2
    #     if c3 > 0:
    #         ans += dp_helper(c1, c2 + 1, c3 - 1, n)*c3
    #     return ans/total + n / total
    # return dp_helper(curr.count(1), curr.count(2), curr.count(3), len(curr))

    n = len(curr)
    c1, c2, c3 = 0, 0, 0
    for plate in curr:
        if plate == 1:
            c1 += 1
        elif plate == 2:
            c2 += 1
        elif plate == 3:
            c3 += 1
    oc1, oc2, oc3 = c1, c2, c3
    c1, c2 = c1 + c2 + c3, c2 + c3

    dp = [[[0.0]*(c1+1) for _ in range(c2+1)] for _ in range(c3+1)]
    for i in range(c3+1):
        for j in range(c2+1):
            for k in range(c1+1):
                if i == 0 and j == 0 and k == 0:
                    dp[i][j][k] = 0.0
                else:
                    total = i + j + k
                    expected = 0.0
                    if k > 0:
                        expected += dp[i][j][k-1] * k
                    if j > 0 and k+1 <= c1:
                        expected += dp[i][j-1][k+1] * j
                    if i > 0 and j+1 <= c2:
                        expected += dp[i-1][j+1][k] * i
                    dp[i][j][k] = expected / total + n / total
    return dp[oc3][oc2][oc1]



n = int(input())
plates = tuple(map(int, input().split()))
print(helper(plates))