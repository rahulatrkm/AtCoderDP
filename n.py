'''
ps - https://atcoder.jp/contests/dp/tasks/dp_n
'''

def helper(arr):
    # n = len(arr)
    # if n == 1:
    #     return 0
    # curr = 0
    # for i in range(n-1):
    #     if arr[i]+arr[i+1] < arr[curr]+arr[curr+1]:
    #         curr = i
    # val = arr[curr] + arr[curr+1]
    # del arr[curr]
    # arr[curr] = val
    # return val + helper(arr)

    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
    
    for length in range(2, n):
        j, k = 0, length
        while k < n:
            dp[j][k] = float('inf')
            for cut in range(j, k):
                dp[j][k] = min(dp[j][k], dp[j][cut] + dp[cut+1][k])
            dp[j][k] += sum(arr[j:k+1])
            j += 1
            k += 1
    return dp[0][n-1]


n = int(input())
arr = list(map(int, input().split()))
print(helper(arr))

# n = 400
# arr = [10**9]*n
# print(helper(arr))