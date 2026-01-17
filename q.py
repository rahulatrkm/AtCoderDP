'''
ps - https://atcoder.jp/contests/dp/tasks/dp_q
'''

def solve():
    n = int(input())
    height = list(map(int, input().split()))
    beauty = list(map(int, input().split()))
    
    seg = [0] * (4 * n)
    
    def update(idx, val, node, node_lb, node_ub):
        if node_lb == node_ub:
            seg[node] = max(seg[node], val)
            return
        mid = (node_lb + node_ub) // 2
        if idx <= mid:
            update(idx, val, 2 * node + 1, node_lb, mid)
        else:
            update(idx, val, 2 * node + 2, mid + 1, node_ub)
        seg[node] = max(seg[2 * node + 1], seg[2 * node + 2])
    
    def query(l, r, node, node_lb, node_ub):
        if r < node_lb or l > node_ub:
            return 0
        if l <= node_lb and node_ub <= r:
            return seg[node]
        mid = (node_lb + node_ub) // 2
        left = query(l, r, 2 * node + 1, node_lb, mid)
        right = query(l, r, 2 * node + 2, mid + 1, node_ub)
        return max(left, right)
    
    for i in range(n):
        best = query(0, height[i] - 1, 0, 0, n - 1)
        update(height[i], best + beauty[i], 0, 0, n - 1)
    
    print(query(0, n - 1, 0, 0, n - 1))

solve()