'''
ps - https://atcoder.jp/contests/dp/tasks/dp_i
'''

def helper(idx, cnt):
    # n = len(probabilities)
    # if idx == n:
    #     if cnt > n/2:
    #         return 1
    #     else:
    #         return 0
    # return helper(idx + 1, cnt + 1)*probabilities[idx] + helper(idx + 1, cnt)*(1 - probabilities[idx])

    n = len(probabilities)
    dp = [0]*(n+1)
    dp[0] = 1.0
    for i in range(1, n+1):
        curr = dp.copy()
        for j in range(0, i+1):
            dp[j] = curr[j]*(1 - probabilities[i-1])
            if j > 0:
                dp[j] += curr[j-1]*probabilities[i-1]
    ans = 0.0
    for j in range(n//2 + 1, n+1):
        ans += dp[j]
    return ans    

n = int(input())
probabilities = list(map(float, input().split()))
print(helper(0, 0))
