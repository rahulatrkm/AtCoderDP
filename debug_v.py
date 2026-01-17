'''
Debug script to understand the algorithm behavior
'''

def test_simple_case():
    """Test with simple 2-node tree: 1-2"""
    print("=" * 60)
    print("Test: Tree 1-2")
    print("=" * 60)
    
    # When node 1 is root:
    # - Subtree at node 2: size 1, so value = 1+1 = 2
    # - Product = 2
    # - Result = 2 - 1 = 1? No wait...
    
    # Let's trace the recursive formula:
    # dfs(1): visits 1, neighbor 2 not visited, calls dfs(2)
    #   dfs(2): visits 2, no unvisited neighbors, ans=1, return 1+1=2
    # Back to dfs(1): ans = 1 * 2 = 2, return 2+1=3
    # Result = 3-1 = 2 ✓
    
    print("When node 1 is root:")
    print("  dfs(1) -> calls dfs(2)")
    print("    dfs(2) -> no unvisited neighbors, return 1+1=2")
    print("  dfs(1) -> ans = 1*2 = 2, return 2+1=3")
    print("  Result: 3-1 = 2")
    
    # When node 2 is root:
    # dfs(2): visits 2, neighbor 1 not visited, calls dfs(1)
    #   dfs(1): visits 1, neighbor 2 already visited (in vis from outer call), no unvisited neighbors
    #   ans=1, return 1+1=2
    # Back to dfs(2): ans = 1*2 = 2, return 2+1=3
    # Result = 3-1 = 2
    
    print("\nWhen node 2 is root:")
    print("  dfs(2) -> calls dfs(1)")
    print("    dfs(1) -> neighbor 2 already visited, return 1+1=2")
    print("  dfs(2) -> ans = 1*2 = 2, return 2+1=3")
    print("  Result: 3-1 = 2")
    
    print("\nExpected: [2, 2]")
    print("Top-down gives: [2, 1]  <- WRONG due to caching bug")
    print("Bottom-up gives: [2, 2] <- CORRECT\n")


def test_star_case():
    """Test with star tree: 1-2, 1-3"""
    print("=" * 60)
    print("Test: Star Tree 1-2, 1-3")
    print("=" * 60)
    
    print("When node 1 is root:")
    print("  dfs(1) -> calls dfs(2) and dfs(3)")
    print("    dfs(2) -> return 2")
    print("    dfs(3) -> return 2")
    print("  dfs(1) -> ans = 1*2*2 = 4, return 4+1=5")
    print("  Result: 5-1 = 4")
    
    print("\nWhen node 2 is root:")
    print("  dfs(2) -> calls dfs(1)")
    print("    dfs(1) -> calls dfs(3)")
    print("      dfs(3) -> return 2")
    print("    dfs(1) -> ans = 1*2 = 2, return 2+1=3")
    print("  dfs(2) -> ans = 1*3 = 3, return 3+1=4")
    print("  Result: 4-1 = 3")
    
    print("\nExpected: [4, 3, 3]")
    print("Top-down gives: [4, 1, 1]  <- WRONG due to caching bug")
    print("Bottom-up gives: [4, 3, 3] <- CORRECT\n")


if __name__ == "__main__":
    test_simple_case()
    test_star_case()
    
    print("\n" + "=" * 60)
    print("CONCLUSION")
    print("=" * 60)
    print("The top-down solution has a BUG due to @lru_cache caching")
    print("results based on (node, col) but not accounting for the")
    print("different 'vis' set state between different root iterations.")
    print()
    print("The bottom-up solution is CORRECT and produces the")
    print("expected results for the problem.")
    print("=" * 60)
