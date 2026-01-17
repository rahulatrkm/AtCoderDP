'''
ps - https://atcoder.jp/contests/dp/tasks/dp_u
'''

# grps = []
# def helper(idx):
#     n = len(arr)
#     if idx == n:
#         ans = 0
#         for g in grps:
#             for i in range(len(g)):
#                 for j in range(i+1, len(g)):
#                     ri, rj = g[i], g[j]
#                     ans += arr[ri][rj]
#         return ans
#     # Option 1: Start new group
#     grps.append([idx])
#     ans1 = helper(idx + 1)
#     grps.pop()
#     # Option 2: Add to existing groups
#     ans2 = 0
#     for g in grps:
#         g.append(idx)
#         ans2 = max(ans2, helper(idx + 1))
#         g.pop()
#     return max(ans1, ans2)

def helper():
    n = len(arr)
    tot = 1 << n
    dp = [0]*tot
    for mask in range(tot):
        members = []
        for i in range(n):
            if (1 << i) & mask:
                members.append(i)
        # Calculate score for current group
        score = 0
        for i in range(len(members)):
            for j in range(i+1, len(members)):
                ri, rj = members[i], members[j]
                score += arr[ri][rj]
        dp[mask] = score
    
    for mask in range(tot):
        submask = mask
        while submask:
            dp[mask] = max(dp[mask], dp[submask] + dp[mask ^ submask])
            submask = (submask - 1) & mask
    return dp[-1]


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
print(helper())