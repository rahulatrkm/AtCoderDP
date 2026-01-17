'''
ps - https://atcoder.jp/contests/dp/tasks/dp_u
'''

def solve():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    tot = 1 << n
    dp = [0] * tot
    
    for mask in range(tot):
        members = [i for i in range(n) if (1 << i) & mask]
        score = 0
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                score += arr[members[i]][members[j]]
        dp[mask] = score
    
    for mask in range(tot):
        submask = mask
        while submask:
            dp[mask] = max(dp[mask], dp[submask] + dp[mask ^ submask])
            submask = (submask - 1) & mask
    
    print(dp[-1])

solve()