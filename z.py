'''
ps - https://atcoder.jp/contests/dp/tasks/dp_z
'''

def solve():
    n, c = map(int, input().split())
    h = list(map(int, input().split()))
    
    hull = []
    dp = [0] * n
    
    def add(m, b):
        while len(hull) >= 2:
            m1, b1 = hull[-2]
            m2, b2 = hull[-1]
            if (b - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m):
                hull.pop()
            else:
                break
        hull.append((m, b))
    
    ptr = 0
    add(-2 * h[0], h[0] * h[0])
    
    for i in range(1, n):
        while ptr + 1 < len(hull) and hull[ptr][0] * h[i] + hull[ptr][1] >= hull[ptr + 1][0] * h[i] + hull[ptr + 1][1]:
            ptr += 1
        dp[i] = h[i] * h[i] + c + hull[ptr][0] * h[i] + hull[ptr][1]
        add(-2 * h[i], dp[i] + h[i] * h[i])
    
    print(dp[-1])

solve()