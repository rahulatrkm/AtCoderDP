'''
ps - https://atcoder.jp/contests/dp/tasks/dp_z
'''

# Original O(N^2) solution
# def helper():
#     n = len(heights)
#     dp = [float('inf')]*n
#     dp[0] = 0
#     for i in range(1, n):
#         for j in range(i):
#             dp[i] = min(dp[i], dp[j] + (heights[i]-heights[j])**2 + c)
#     return dp[-1]

# n, c = map(int, input().split())
# heights = list(map(int, input().split()))
# print(helper())


'''
Optimized: O(N) using Convex Hull Trick (CHT)
dp[i] = h[i]^2 + c + min(-2*h[j]*h[i] + dp[j] + h[j]^2)
'''

def solve():
    n, c = map(int, input().split())
    h = list(map(int, input().split()))
    
    # hull stores (slope, intercept) pairs
    hull = []
    dp = [0] * n
    
    def add(m, b):
        # Remove lines that become useless
        while len(hull) >= 2:
            m1, b1 = hull[-2]
            m2, b2 = hull[-1]
            # Check if last line is dominated
            if (b - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m):
                hull.pop()
            else:
                break
        hull.append((m, b))
    
    ptr = 0
    add(-2 * h[0], h[0] * h[0])
    
    for i in range(1, n):
        # Move pointer to best line (since h is increasing, pointer only moves right)
        while ptr + 1 < len(hull) and hull[ptr][0] * h[i] + hull[ptr][1] >= hull[ptr+1][0] * h[i] + hull[ptr+1][1]:
            ptr += 1
        dp[i] = h[i] * h[i] + c + hull[ptr][0] * h[i] + hull[ptr][1]
        add(-2 * h[i], dp[i] + h[i] * h[i])
    
    print(dp[-1])

solve()