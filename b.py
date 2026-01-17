'''
ps - https://atcoder.jp/contests/dp/tasks/dp_b
'''

def frog_jump_cost(n, k, heights):
    dp = [float('inf')]*n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, min(k, i)+1):
            dp[i] = min(dp[i], dp[i-j] + abs(heights[i] - heights[i-j]))
    return dp[-1]

n, k = map(int, input().split())
ht = list(map(int, input().split()))
print(frog_jump_cost(n, k, ht))