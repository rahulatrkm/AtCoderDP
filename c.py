'''
ps - https://atcoder.jp/contests/dp/tasks/dp_c
'''

def helper():
    # if idx == len(points):
    #     return 0
    # ans = 0
    # if last != 0:
    #     ans = max(ans, helper(idx + 1, 0) + points[idx][0])
    # if last != 1:
    #     ans = max(ans, helper(idx + 1, 1) + points[idx][1])
    # if last != 2:
    #     ans = max(ans, helper(idx + 1, 2) + points[idx][2])
    # return ans
    n = len(points)
    dp = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + points[i-1][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + points[i-1][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + points[i-1][2]
    return max(dp[n])




n = int(input())
points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))

print(helper())