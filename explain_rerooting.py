'''
Understanding the 2nd DFS in Rerooting DP
'''

import collections

def explain_rerooting():
    print("=" * 80)
    print("UNDERSTANDING REROOTING DP - Second DFS")
    print("=" * 80)
    
    # Simple example: Tree with 5 nodes
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    
    n = 4
    edges = [(1, 2), (1, 3), (2, 4)]
    m = 1000
    
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    print("\nExample Tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    /")
    print("   4")
    print()
    
    # First DFS - compute subtree products
    dp1 = [1] * (n + 1)
    
    def dfs1(node, parent):
        prod = 1
        for child in adj[node]:
            if child != parent:
                dfs1(child, node)
                prod = (prod * dp1[child]) % m
        dp1[node] = (1 + prod) % m
        return dp1[node]
    
    print("=" * 80)
    print("STEP 1: First DFS (compute subtree products from root=1)")
    print("=" * 80)
    
    dfs1(1, -1)
    
    print("\ndp1[node] = (1 + product of all child subtrees)")
    print()
    print("Computing bottom-up:")
    print("  Node 4: leaf, no children → dp1[4] = 1 + 0 = 1")
    print("  Node 3: leaf, no children → dp1[3] = 1 + 0 = 1")  
    print("  Node 2: has child 4 → dp1[2] = 1 + dp1[4] = 1 + 2 = 3")
    print("  Node 1: has children 2,3 → dp1[1] = 1 + (dp1[2] * dp1[3]) = 1 + (3*2) = 7")
    print()
    print(f"Result: dp1 = {[dp1[i] for i in range(1, n+1)]}")
    print()
    print("dp1[1] - 1 = 6 is the answer when node 1 is root!")
    
    print("\n" + "=" * 80)
    print("STEP 2: Second DFS (reroot to compute ALL nodes as root)")
    print("=" * 80)
    
    print("\nKey Insight:")
    print("  When we move root from PARENT to CHILD, we need to:")
    print("  1. Remove child's contribution from parent")
    print("  2. Add parent's (new) contribution to child")
    print()
    
    ans = [0] * (n + 1)
    
    print("Let's trace dfs2 step by step:")
    print()
    
    def dfs2_explained(node, parent, parent_contribution, depth=0):
        indent = "  " * depth
        print(f"{indent}╔══ dfs2(node={node}, parent={parent}, parent_contrib={parent_contribution})")
        
        # Calculate answer for this node as root
        prod = parent_contribution
        children_info = []
        for child in adj[node]:
            if child != parent:
                children_info.append(f"child {child} (dp1={dp1[child]})")
                prod = (prod * dp1[child]) % m
        
        ans[node] = prod % m
        
        print(f"{indent}║")
        print(f"{indent}║ Children: {', '.join(children_info) if children_info else 'none'}")
        print(f"{indent}║ Answer[{node}] = parent_contrib * products")
        print(f"{indent}║            = {parent_contribution} * {prod // parent_contribution if parent_contribution > 0 else prod}")
        print(f"{indent}║            = {ans[node]}")
        print(f"{indent}║")
        
        # Reroot to each child
        for child in adj[node]:
            if child != parent:
                print(f"{indent}║ → Now rerooting from {node} to {child}...")
                print(f"{indent}║")
                
                # Calculate what node contributes when child becomes root
                # Remove child's contribution
                remaining = parent_contribution
                for other_child in adj[node]:
                    if other_child != parent and other_child != child:
                        remaining = (remaining * dp1[other_child]) % m
                
                node_contribution = (1 + remaining) % m
                
                print(f"{indent}║   When {child} is root, {node} becomes its parent")
                print(f"{indent}║   {node}'s contribution = 1 + (parent_contrib * other_children)")
                print(f"{indent}║                        = 1 + {remaining}")
                print(f"{indent}║                        = {node_contribution}")
                print(f"{indent}║")
                
                dfs2_explained(child, node, node_contribution, depth + 1)
        
        print(f"{indent}╚══ Finished dfs2(node={node})")
        print()
    
    dfs2_explained(1, -1, 1)
    
    print("=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    print()
    for i in range(1, n + 1):
        print(f"  Node {i} as root: ans[{i}] = {ans[i]}")
    
    print()
    print("=" * 80)
    print("WHY SECOND DFS WORKS")
    print("=" * 80)
    print()
    print("1. First DFS gives us subtree products when node 1 is root")
    print("   → dp1[child] = answer for subtree below 'child'")
    print()
    print("2. Second DFS 'moves' the root around:")
    print("   → When moving from parent to child:")
    print("     • Child no longer sees parent as 'above'")
    print("     • Parent becomes just another subtree 'below' child")
    print()
    print("3. parent_contribution = what parent gives to child")
    print("   → It's calculated as: (1 + all other subtrees from parent)")
    print()
    print("4. By recursively rerooting, we visit each node as root exactly once")
    print("   → Total time: O(N) instead of O(N²)!")
    print()
    print("=" * 80)


def visualize_rerooting():
    print("\n" + "=" * 80)
    print("VISUAL EXAMPLE: Tree Structure Changes During Rerooting")
    print("=" * 80)
    
    print("\nOriginal tree (root=1):")
    print("       1")
    print("      ↙ ↘")
    print("     2   3")
    print("    ↙")
    print("   4")
    print("\nSubtrees when root=1:")
    print("  Node 1 sees: subtree(2)={2,4}, subtree(3)={3}")
    print("  Answer[1] = (1+dp1[2]) * (1+dp1[3])")
    print()
    
    print("When we reroot to node 2:")
    print("       2")
    print("      ↙ ↘")
    print("     4   1")
    print("          ↘")
    print("           3")
    print("\nSubtrees when root=2:")
    print("  Node 2 sees: subtree(4)={4}, subtree(1)={1,3}")
    print("  Answer[2] = (1+dp1[4]) * (1+contribution_from_1)")
    print("  where contribution_from_1 = (1 + dp1[3])")
    print()
    
    print("When we reroot to node 3:")
    print("       3")
    print("        ↘")
    print("         1")
    print("        ↙")
    print("       2")
    print("      ↙")
    print("     4")
    print("\nSubtrees when root=3:")
    print("  Node 3 sees: subtree(1)={1,2,4}")
    print("  Answer[3] = (1 + contribution_from_1)")
    print("  where contribution_from_1 = (1 + dp1[2])")
    print()
    
    print("This is why we can compute all answers in O(N)!")
    print("We reuse dp1 values and just adjust for the parent contribution.")
    print("=" * 80)


if __name__ == "__main__":
    explain_rerooting()
    visualize_rerooting()
