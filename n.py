'''
ps - https://atcoder.jp/contests/dp/tasks/dp_n
'''

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i + 1] = arr[i] + arr[i + 1]
    
    for length in range(2, n):
        for j in range(n - length):
            k = j + length
            dp[j][k] = float('inf')
            for cut in range(j, k):
                dp[j][k] = min(dp[j][k], dp[j][cut] + dp[cut + 1][k])
            dp[j][k] += prefix[k + 1] - prefix[j]
    
    print(dp[0][n - 1])

solve()