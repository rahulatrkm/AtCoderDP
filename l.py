'''
ps - https://atcoder.jp/contests/dp/tasks/dp_l
'''

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = arr[i]
    for i in range(n - 1):
        dp[i][i + 1] = max(arr[i], arr[i + 1])
    
    for length in range(2, n):
        j, k = 0, length
        while k < n:
            dp[j][k] = max(arr[j] + min(dp[j + 2][k] if j + 2 <= k else 0, dp[j + 1][k - 1]),
                           arr[k] + min(dp[j + 1][k - 1], dp[j][k - 2] if k - 2 >= j else 0))
            j += 1
            k += 1
    
    fp = dp[0][n - 1]
    print(2 * fp - sum(arr))

solve()