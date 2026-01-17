'''
EDGE CASE that will BREAK your code!
'''

from functools import lru_cache
import collections

print("=" * 80)
print("EDGE CASE: MULTIPLE TEST CASES WITHOUT CACHE CLEAR")
print("=" * 80)

def your_code_with_persistent_cache(test_cases):
    """
    Simulates running multiple test cases with the SAME cache
    (like in competitive programming when cache isn't cleared)
    """
    
    # Single persistent cache across test cases
    @lru_cache(None)
    def dfs(node, col, par):
        vis.add(node)
        if col == 0:
            return 1
        ans = 1
        for ne in adj[node]:
            if ne in vis:
                continue
            ans *= dfs(ne, col, node)
        return ans + 1
    
    results = []
    
    for test_num, (n, edges, m) in enumerate(test_cases, 1):
        print(f"\nTest case {test_num}:")
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = []
        for i in range(1, n+1):
            vis = set()
            res.append((dfs(i, 1, -1)-1) % m)
        
        print(f"  Result: {res}")
        results.append(res)
        print(f"  Cache size: {dfs.cache_info().currsize}")
    
    return results


# Test case 1: Simple tree
test1 = (3, [(1, 2), (2, 3)], 100)
# Test case 2: SAME STRUCTURE but different node numbering
test2 = (3, [(1, 2), (2, 3)], 100)

print("\nRunning multiple test cases WITH PERSISTENT CACHE:")
print("(This simulates what happens in competitive programming)")
your_results = your_code_with_persistent_cache([test1, test2])

print("\n" + "=" * 80)
print("EXPECTED vs ACTUAL")
print("=" * 80)
print("Both test cases should give: [3, 4, 3]")
print(f"Test 1: {your_results[0]} - {'✓' if your_results[0] == [3, 4, 3] else '✗'}")
print(f"Test 2: {your_results[1]} - {'✓' if your_results[1] == [3, 4, 3] else '✗'}")

print("\n" + "=" * 80)
print("ANOTHER EDGE CASE: CALLING HELPER TWICE")
print("=" * 80)

from v import helper

# Clear any previous cache by reimporting
import importlib
import v
importlib.reload(v)
from v import helper

n, m = 3, 100
edges = [(1, 2), (2, 3)]

print(f"\nFirst call to helper({n}, {edges}, {m}):")
result1 = helper(n, edges, m)
print(f"Result: {result1}")

print(f"\nSecond call to helper({n}, {edges}, {m}):")
result2 = helper(n, edges, m)
print(f"Result: {result2}")

print(f"\nMatch: {'✓' if result1 == result2 else '✗ CACHE BUG!'}")

print("\n" + "=" * 80)
print("THE REAL EDGE CASE:")
print("=" * 80)
print("Your code actually WORKS in single-problem scenarios because:")
print("  1. Cache is cleared between problem submissions")
print("  2. vis is reset for each root within a test case")
print("  3. par parameter provides enough context")
print()
print("But it COULD FAIL if:")
print("  ✗ Running multiple test cases in one program (batch testing)")
print("  ✗ Cache persists across different inputs")
print("  ✗ You forget to reset vis between roots")
print()
print("CONCEPTUAL ISSUE:")
print("  Mixing SIDE EFFECTS (vis.add) with PURE CACHING (@lru_cache)")
print("  is fundamentally problematic, even if it works in practice.")
print()
print("RECOMMENDATION:")
print("  Use the bottom-up or tabular solution for cleaner, safer code!")
print("=" * 80)
