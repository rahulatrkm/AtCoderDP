'''
Comprehensive test for Problem G - Longest Path in DAG
Constraints: N ≤ 10^5, M ≤ 10^5 (DAG - Directed Acyclic Graph)
Tests edge cases, time and space complexity
'''

import subprocess
import time
import sys

def run_test(n, edges, expected, description, timeout=5):
    """Run test and measure time"""
    # Format input
    m = len(edges)
    input_str = f"{n} {m}\n"
    input_str += "\n".join(f"{u} {v}" for u, v in edges)
    
    # Create wrapper script that sets recursion limit
    wrapper = f'''
import sys
sys.setrecursionlimit(200000)
exec(open("g.py").read())
'''
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', '-c', wrapper],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd='/Users/rahul./Downloads/AtCoderDP'
        )
        elapsed = time.time() - start
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED")
            print(f"   Error: {result.stderr[:200]}")
            return False
        
        output = int(result.stdout.strip())
        passed = output == expected
        status = "✓" if passed else "✗"
        time_icon = "⚡" if elapsed < 0.5 else "🐌" if elapsed > 2 else "⏱️"
        
        print(f"{status} {time_icon} {description}")
        print(f"   Result: {output} (Expected: {expected}) [{elapsed:.3f}s]")
        return passed
        
    except subprocess.TimeoutExpired:
        print(f"✗ ⏰ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ ❌ {description}: ERROR - {str(e)}")
        return False

print("="*80)
print("PROBLEM G: Longest Path in DAG")
print("Constraints: N ≤ 10^5, M ≤ 10^5")
print("="*80)

passed = 0
total = 0

# Sample tests
print("\n[Sample Tests]")
total += 1
passed += run_test(4, [(1,2), (1,3), (3,2), (2,4), (3,4)], 3, "Sample 1")

total += 1
passed += run_test(6, [(2,3), (4,5), (5,6)], 2, "Sample 2: Multiple components")

# Edge cases
print("\n[Edge Cases]")
total += 1
passed += run_test(1, [], 0, "Single node, no edges")

total += 1
passed += run_test(2, [], 0, "Two nodes, no edges")

total += 1
passed += run_test(2, [(1,2)], 1, "Single edge")

total += 1
passed += run_test(3, [(1,2), (2,3)], 2, "Simple path")

total += 1
passed += run_test(10, [], 0, "10 nodes, no edges")

# Linear chain (worst case for depth)
print("\n[Linear Chain Tests]")
total += 1
linear_10 = [(i, i+1) for i in range(1, 10)]
passed += run_test(10, linear_10, 9, "Linear chain: 10 nodes")

total += 1
linear_100 = [(i, i+1) for i in range(1, 100)]
passed += run_test(100, linear_100, 99, "Linear chain: 100 nodes")

total += 1
linear_1000 = [(i, i+1) for i in range(1, 1000)]
passed += run_test(1000, linear_1000, 999, "Linear chain: 1000 nodes")

# Star graph (one node connects to all others)
print("\n[Star Graph Tests]")
total += 1
star_10 = [(1, i) for i in range(2, 11)]
passed += run_test(10, star_10, 1, "Star: 1 node to 9 nodes")

total += 1
star_100 = [(1, i) for i in range(2, 101)]
passed += run_test(100, star_100, 1, "Star: 1 node to 99 nodes")

# Complete DAG (all edges i->j where i<j)
print("\n[Dense Graph Tests]")
total += 1
complete_10 = [(i, j) for i in range(1, 10) for j in range(i+1, 11)]
passed += run_test(10, complete_10, 9, f"Complete DAG: 10 nodes, {len(complete_10)} edges")

total += 1
complete_20 = [(i, j) for i in range(1, 20) for j in range(i+1, 21)]
passed += run_test(20, complete_20, 19, f"Complete DAG: 20 nodes, {len(complete_20)} edges")

# Binary tree structure
print("\n[Binary Tree Tests]")
total += 1
# Perfect binary tree depth 3 (15 nodes): 1->2->4->8 = 3 edges
binary_tree = []
for i in range(1, 8):
    binary_tree.append((i, 2*i))
    binary_tree.append((i, 2*i+1))
passed += run_test(15, binary_tree, 3, "Binary tree: depth 3 (15 nodes)")

# Diamond pattern (multiple paths)
print("\n[Multiple Paths Tests]")
total += 1
diamond = [(1,2), (1,3), (1,4), (2,5), (3,5), (4,5)]
passed += run_test(5, diamond, 2, "Diamond: multiple paths same length")

total += 1
complex_dag = [(1,2), (1,3), (2,4), (2,5), (3,5), (3,6), (4,7), (5,7), (6,7)]
passed += run_test(7, complex_dag, 3, "Complex DAG: multiple paths")

# Performance tests
print("\n[Performance Tests - Time & Space]")

# Test 1: Large linear chain
total += 1
linear_10k = [(i, i+1) for i in range(1, 10000)]
passed += run_test(10000, linear_10k, 9999, "10K nodes linear chain", timeout=3)

# Test 2: Large star graph
total += 1
star_10k = [(1, i) for i in range(2, 10001)]
passed += run_test(10000, star_10k, 1, "10K nodes star graph", timeout=3)

# Test 3: Max nodes with moderate edges
total += 1
# Create a graph with 100K nodes, edges forming chains
edges_100k = []
for chain in range(100):  # 100 chains of 1000 nodes
    start = chain * 1000 + 1
    for i in range(start, start + 999):
        edges_100k.append((i, i+1))
passed += run_test(100000, edges_100k, 999, "100K nodes, 99.9K edges (chains)", timeout=5)

# Test 4: Max nodes max edges scenario
print("\n⚠️  Maximum constraint test:")
total += 1
# Binary tree-like structure to max nodes and edges
edges_max = []
for i in range(1, 50001):
    if 2*i <= 100000:
        edges_max.append((i, 2*i))
    if 2*i+1 <= 100000:
        edges_max.append((i, 2*i+1))
passed += run_test(100000, edges_max, 16, f"100K nodes, {len(edges_max)} edges (binary tree)", timeout=5)

# Summary
print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Tests Passed: {passed}/{total}")
print(f"\nComplexity Analysis:")
print(f"  Time: O(N + M) - DFS with memoization")
print(f"  Space: O(N + M) - adjacency list + DP array + recursion stack")
print(f"  Max: N=10^5, M=10^5 (manageable)")
print("="*80)
