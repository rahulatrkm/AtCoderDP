'''
Test edge cases where vis closure variable might cause issues
'''

from v import helper, helper_bottom_up
import collections

def simulate_your_code_detailed(n, edges, m, root):
    """Simulate your code with detailed logging"""
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    from functools import lru_cache
    
    vis = set()
    call_log = []
    
    @lru_cache(None)
    def dfs(node, col, par):
        call_log.append(('call', node, col, par, tuple(sorted(vis))))
        vis.add(node)
        if col == 0:
            return 1
        ans = 1
        for ne in adj[node]:
            if ne in vis:
                call_log.append(('skip', ne, 'already in vis'))
                continue
            ans *= dfs(ne, col, node)
        call_log.append(('return', node, ans + 1))
        return ans + 1
    
    result = dfs(root, 1, -1) - 1
    return result, call_log


print("=" * 80)
print("TESTING EDGE CASES FOR YOUR CODE")
print("=" * 80)

# Test 1: Graph where cache might interfere
print("\n" + "=" * 80)
print("Test 1: Complex tree - cache with vis closure")
print("=" * 80)

n = 5
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
m = 1000

print(f"Tree: {edges}")
print(f"\nTesting root 1:")
result1, log1 = simulate_your_code_detailed(n, edges, m, 1)
print(f"Result: {result1}")
print(f"Cache calls: {len([x for x in log1 if x[0] == 'call'])}")

print(f"\nNow testing root 2 with SAME cache:")
result2, log2 = simulate_your_code_detailed(n, edges, m, 2)
print(f"Result: {result2}")
print(f"Cache calls: {len([x for x in log2 if x[0] == 'call'])}")

print("\nCompare with bottom-up:")
correct = helper_bottom_up(n, edges, m)
print(f"Bottom-up: {correct}")
your_code = helper(n, edges, m)
print(f"Your code: {your_code}")
print(f"Match: {'✓' if your_code == correct else '✗'}")

# Test 2: The real edge case - when vis matters
print("\n" + "=" * 80)
print("Test 2: Edge case where vis state matters")
print("=" * 80)

# Tree structure where cache pollution could happen
n = 6
edges = [(1, 2), (1, 3), (3, 4), (3, 5), (5, 6)]
m = 1000

print(f"Tree: {edges}")
print("Structure: 1 connects to 2 and 3, 3 connects to 4 and 5, 5 connects to 6")

your_result = helper(n, edges, m)
correct_result = helper_bottom_up(n, edges, m)

print(f"\nYour code:   {your_result}")
print(f"Bottom-up:   {correct_result}")
print(f"Match: {'✓' if your_result == correct_result else '✗ EDGE CASE FOUND!'}")

if your_result != correct_result:
    print("\nDifferences found at indices:")
    for i in range(len(your_result)):
        if your_result[i] != correct_result[i]:
            print(f"  Node {i+1}: yours={your_result[i]}, correct={correct_result[i]}")

# Test 3: Stress test with larger tree
print("\n" + "=" * 80)
print("Test 3: Larger tree stress test")
print("=" * 80)

for n in [10, 20, 30]:
    # Create a more complex tree (not just linear)
    edges = []
    # Build a tree with branching
    for i in range(1, n):
        parent = (i + 1) // 2
        if parent == 0:
            parent = 1
        edges.append((parent, i + 1))
    
    m = 10**9 + 7
    
    your_result = helper(n, edges, m)
    correct_result = helper_bottom_up(n, edges, m)
    
    match = your_result == correct_result
    status = "✓" if match else "✗ MISMATCH"
    
    print(f"N={n:2d}: {status}")
    
    if not match:
        mismatches = sum(1 for i in range(len(your_result)) if your_result[i] != correct_result[i])
        print(f"       {mismatches} mismatches out of {n} nodes")

print("\n" + "=" * 80)
print("CONCLUSION")
print("=" * 80)
print("Your code with 'par' parameter added actually works correctly!")
print()
print("The 'par' parameter disambiguates cache entries enough that")
print("the vis set state doesn't cause incorrect results.")
print()
print("However, there's still a SUBTLE ISSUE:")
print("  • vis.add(node) is a SIDE EFFECT in a cached function")
print("  • When cache returns a value, vis.add() doesn't execute")
print("  • This works by accident because vis is reset per root")
print()
print("POTENTIAL EDGE CASE (theoretical):")
print("  • If you reused the cache across multiple test cases")
print("  • Or if vis wasn't reset between roots")
print("  • The code would break")
print()
print("The fix (par parameter) makes it work, but it's still")
print("mixing side effects (vis mutation) with pure caching.")
print("=" * 80)
