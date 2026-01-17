"""
ps - https://atcoder.jp/contests/dp/tasks/dp_w

Given N positions and M queries (l, r, a), choose where to place '1's in a 
binary string to maximize score. Query (l,r,a) adds 'a' if any '1' exists in [l,r].

Solution: DP with lazy segment tree
- dp[i] = max score with rightmost '1' at position i
- Process positions left-to-right using coordinate compression
- Use segment tree for efficient range-max queries and range-add updates

Time: O(M log M), Space: O(M)
Submit with PyPy3 for performance.
"""


def solve():
    n, m = map(int, input().split())

    # Read queries and collect coordinates for compression
    queries = []
    coords = {0}  # Include 0 for base case
    for _ in range(m):
        l, r, a = map(int, input().split())
        queries.append((l, r, a))
        coords.add(l)
        coords.add(r)

    # Coordinate compression
    coords = sorted(coords)
    compress = {v: i for i, v in enumerate(coords)}
    num_coords = len(coords)

    # Group queries by their right endpoint (compressed)
    queries_by_right = [[] for _ in range(num_coords)]
    for l, r, a in queries:
        queries_by_right[compress[r]].append((compress[l], a))

    # Segment tree with lazy propagation
    # Supports: range add, range max query
    log = num_coords.bit_length()
    tree_size = 1 << log
    tree = [0] * (tree_size * 2)  # Max values
    lazy = [0] * (tree_size * 2)  # Pending additions
    NEG_INF = -10**18

    def push_down(node):
        """Push lazy value to children."""
        if lazy[node]:
            for child in (node * 2, node * 2 + 1):
                tree[child] += lazy[node]
                if child < tree_size:
                    lazy[child] += lazy[node]
            lazy[node] = 0

    def push_path(pos):
        """Push all lazy values on path from root to pos."""
        for shift in range(log, 0, -1):
            ancestor = pos >> shift
            if lazy[ancestor]:
                push_down(ancestor)

    def range_max(left, right):
        """Query max in [left, right)."""
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
        """Add value to all elements in [left, right)."""
        left += tree_size
        right += tree_size
        left_orig, right_orig = left, right
        
        # Update nodes
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
        
        # Rebuild ancestors
        for pos in (left_orig, right_orig - 1):
            while pos > 1:
                pos >>= 1
                tree[pos] = max(tree[pos * 2], tree[pos * 2 + 1]) + lazy[pos]

    # DP: process each coordinate position
    for i in range(num_coords):
        # Propagate: dp[i] = max(dp[i], max(dp[0..i-1]))
        if i > 0:
            best_before = range_max(0, i)
            current = range_max(i, i + 1)
            if best_before > current:
                range_add(i, i + 1, best_before - current)

        # Process all queries ending at position i
        for query_left, score in queries_by_right[i]:
            range_add(query_left, i + 1, score)

    # Answer is max(0, max(dp)) - can always choose empty string for score 0
    print(max(0, range_max(0, num_coords)))


if __name__ == "__main__":
    solve()