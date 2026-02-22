'''
ps - https://atcoder.jp/contests/dp/tasks/dp_q
'''

def helper(beauty, height):
    # n = len(height)
    # dp = [0]*n
    # for i in range(n):
    #     dp[i] = beauty[i]
    #     for j in range(i):
    #         if height[j] < height[i]:
    #             dp[i] = max(dp[i], dp[j] + beauty[i])
    # return max(dp)
    
    n = len(height)
    seg = [0]*(4*n)
    def update(idx, val, node, node_lb, node_ub):
        if node_lb == node_ub:
            seg[node] = max(seg[node], val)
            return
        mid = (node_lb + node_ub)//2
        if idx <= mid:
            update(idx, val, 2*node+1, node_lb, mid)
        else:
            update(idx, val, 2*node+2, mid+1, node_ub)
        seg[node] = max(seg[2*node+1], seg[2*node+2])

    def query(l, r, node, node_lb, node_ub):
        if r < node_lb or l > node_ub:
            return 0
        if l <= node_lb and node_ub <= r:
            return seg[node]
        mid = (node_lb + node_ub)//2
        left = query(l, r, 2*node+1, node_lb, mid)
        right = query(l, r, 2*node+2, mid+1, node_ub)
        return max(left, right)
    
    for i in range(n):
        best = query(0, height[i]-1, 0, 0, n-1)
        update(height[i], best + beauty[i], 0, 0, n-1)
    return query(0, n-1, 0, 0, n-1)

n = int(input())
height = list(map(int, input().split()))
beauty = list(map(int, input().split()))
print(helper(beauty, height))


'''
# With BIT

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

bit = [0]*(n+1)
def update(idx, best):
  idx += 1
  while idx < len(bit):
    bit[idx] = max(bit[idx], best)
    idx += idx & (-idx)

def query(idx):
  best = 0
  idx += 1
  while idx > 0:
    best = max(best, bit[idx])
    idx -= idx & (-idx)
  return best

sor_h = sorted(h)
rank = {v: i for i,v in enumerate(sor_h)}

ans = 0
for i in range(n):
  r = rank[h[i]]
  best = query(r-1) + a[i]
  ans = max(ans, best)
  update(r, best)
  

print(ans)
'''
