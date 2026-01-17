'''
PS - https://atcoder.jp/contests/dp/tasks/dp_a
'''

def frog_jump_cost(n, heights):
    dp = [float('inf')]*n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        dp[i] = min(dp[i], dp[i-1] + abs(heights[i-1] - heights[i]), dp[i-2] + abs(heights[i-2] - heights[i]))
    return dp[-1]
    
n = int(input())
ht = list(map(int, input().split()))
print(frog_jump_cost(n, ht))

