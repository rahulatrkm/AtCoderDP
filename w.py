'''
ps - https://atcoder.jp/contests/dp/tasks/dp_w
'''

def solve():
    n, m = map(int, input().split())
    
    queries = []
    coords = {0}
    for _ in range(m):
        l, r, a = map(int, input().split())
        queries.append((l, r, a))
        coords.add(l)
        coords.add(r)
    
    coords = sorted(coords)
    compress = {v: i for i, v in enumerate(coords)}
    num_coords = len(coords)
    
    queries_by_right = [[] for _ in range(num_coords)]
    for l, r, a in queries:
        queries_by_right[compress[r]].append((compress[l], a))
    
    log = num_coords.bit_length()
    tree_size = 1 << log
    tree = [0] * (tree_size * 2)
    lazy = [0] * (tree_size * 2)
    NEG_INF = -10**18
    
    def push_down(node):
        if lazy[node]:
            for child in (node * 2, node * 2 + 1):
                tree[child] += lazy[node]
                if child < tree_size:
                    lazy[child] += lazy[node]
            lazy[node] = 0
    
    def push_path(pos):
        for shift in range(log, 0, -1):
            ancestor = pos >> shift
            if lazy[ancestor]:
                push_down(ancestor)
    
    def range_max(left, right):
        left += tree_size
        right += tree_size
        push_path(left)
        push_path(right - 1)
        
        result = NEG_INF
        while left < right:
            if left & 1:
                result = max(result, tree[left])
                left += 1
            if right & 1:
                right -= 1
                result = max(result, tree[right])
            left >>= 1
            right >>= 1
        return result
    
    def range_add(left, right, value):
        left += tree_size
        right += tree_size
        left_orig, right_orig = left, right
        
        while left < right:
            if left & 1:
                tree[left] += value
                if left < tree_size:
                    lazy[left] += value
                left += 1
            if right & 1:
                right -= 1
                tree[right] += value
                if right < tree_size:
                    lazy[right] += value
            left >>= 1
            right >>= 1
        
        for pos in (left_orig, right_orig - 1):
            while pos > 1:
                pos >>= 1
                tree[pos] = max(tree[pos * 2], tree[pos * 2 + 1]) + lazy[pos]
    
    for i in range(num_coords):
        if i > 0:
            best_before = range_max(0, i)
            current = range_max(i, i + 1)
            if best_before > current:
                range_add(i, i + 1, best_before - current)
        
        for query_left, score in queries_by_right[i]:
            range_add(query_left, i + 1, score)
    
    print(max(0, range_max(0, num_coords)))

solve()