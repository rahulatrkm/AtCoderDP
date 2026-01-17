'''
ps - https://atcoder.jp/contests/dp/tasks/dp_d
'''

def helper(w):
    dp = [0]*(w+1)
    for item_w, item_v in wv:
        curr = dp.copy()
        for wt in range(item_w, w+1):
            if wt - item_w >= 0:
                dp[wt] = max(dp[wt], curr[wt - item_w] + item_v)
    return dp[-1]

n, w = map(int, input().split())
wv = []
for _ in range(n):
    wv.append(tuple(map(int, input().split())))

print(helper(w))        
