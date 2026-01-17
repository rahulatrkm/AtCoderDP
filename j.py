'''
ps - https://atcoder.jp/contests/dp/tasks/dp_j
'''

def solve():
    n = int(input())
    plates = list(map(int, input().split()))
    
    c1 = plates.count(1)
    c2 = plates.count(2)
    c3 = plates.count(3)
    
    dp = [[[0.0] * (c1 + 1) for _ in range(c2 + 1)] for _ in range(c3 + 1)]
    
    for i in range(c3 + 1):
        for j in range(c2 + 1):
            for k in range(c1 + 1):
                total = i + j + k
                if total == 0:
                    continue
                
                expected = n / total
                if k > 0:
                    expected += dp[i][j][k-1] * k / total
                if j > 0:
                    expected += dp[i][j-1][k+1] * j / total
                if i > 0:
                    expected += dp[i-1][j+1][k] * i / total
                
                dp[i][j][k] = expected
    
    print(dp[c3][c2][c1])

solve()