'''
Large Test Cases - Maximum Constraint Testing
Tests all problems with near-maximum or maximum allowed inputs
'''

import subprocess
import time
import os
import sys

def create_clean_version(original_file, clean_file):
    """Create clean version without test code"""
    clean_versions = {
        'a.py': '''
def frog_jump_cost(n, heights):
    dp = [float('inf')]*n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        dp[i] = min(dp[i], dp[i-1] + abs(heights[i-1] - heights[i]), dp[i-2] + abs(heights[i-2] - heights[i]))
    return dp[-1]

n = int(input())
heights = list(map(int, input().split()))
print(frog_jump_cost(n, heights))
''',
        'b.py': '''
def frog_jump_cost(n, k, heights):
    dp = [float('inf')]*n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, min(k, i)+1):
            dp[i] = min(dp[i], dp[i-j] + abs(heights[i] - heights[i-j]))
    return dp[-1]

n, k = map(int, input().split())
heights = list(map(int, input().split()))
print(frog_jump_cost(n, k, heights))
''',
        'c.py': open('/Users/rahul./Downloads/AtCoderDP/c.py').read(),
        'd.py': open('/Users/rahul./Downloads/AtCoderDP/d.py').read(),
        'e.py': open('/Users/rahul./Downloads/AtCoderDP/e.py').read()
    }
    
    with open(clean_file, 'w') as f:
        f.write(clean_versions[original_file])

def run_large_test(file, input_str, description, timeout=10):
    """Run large test case"""
    clean_file = f"_test_{file}"
    
    try:
        create_clean_version(file, clean_file)
        
        print(f"\n{'='*70}")
        print(f"Testing: {description}")
        print(f"{'='*70}")
        
        # Calculate input size
        input_lines = input_str.strip().split('\n')
        input_size = len(input_str)
        print(f"📊 Input size: {input_size:,} bytes, {len(input_lines):,} lines")
        
        start_time = time.time()
        result = subprocess.run(
            ['python3', clean_file],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            print(f"❌ CRASHED")
            print(f"Error: {result.stderr[:200]}")
            return False
        
        output = result.stdout.strip()
        time_status = "⚡" if elapsed < 1 else "⏱️" if elapsed < 3 else "🐌"
        
        print(f"✅ PASSED")
        print(f"{time_status} Time: {elapsed:.3f}s")
        print(f"📤 Output: {output}")
        
        if elapsed > 5:
            print(f"⚠️  Warning: Slow execution (>{elapsed:.1f}s)")
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"❌ TIMEOUT (>{timeout}s)")
        print(f"⚠️  Solution cannot handle this input size")
        return False
    except MemoryError:
        print(f"❌ OUT OF MEMORY")
        print(f"⚠️  Solution exhausted available memory")
        return False
    except Exception as e:
        print(f"❌ ERROR: {str(e)[:200]}")
        return False
    finally:
        if os.path.exists(clean_file):
            os.remove(clean_file)

print("="*80)
print("LARGE TEST CASES - MAXIMUM CONSTRAINT TESTING")
print("="*80)
print("Testing with maximum or near-maximum allowed inputs per problem constraints")
print("="*80)

results = []

# PROBLEM A: N ≤ 10^5
print("\n" + "="*80)
print("PROBLEM A: Frog 1")
print("Constraint: N ≤ 100,000")
print("="*80)

# Test 1: N = 100,000 (maximum)
n = 100000
heights = [(i * 123 + 456) % 10000 + 1 for i in range(n)]
input_a1 = f"{n}\n" + " ".join(map(str, heights))
result_a1 = run_large_test('a.py', input_a1, "N=100,000 (maximum)", timeout=5)
results.append(("Problem A - N=100K", result_a1))

# Test 2: Worst case - alternating extremes
heights_worst = [1, 10000] * 50000
input_a2 = f"100000\n" + " ".join(map(str, heights_worst))
result_a2 = run_large_test('a.py', input_a2, "N=100,000 alternating 1↔10000", timeout=5)
results.append(("Problem A - Worst case", result_a2))

# PROBLEM B: N ≤ 10^5, K ≤ 100
print("\n" + "="*80)
print("PROBLEM B: Frog 2")
print("Constraint: N ≤ 100,000, K ≤ 100")
print("="*80)

# Test 1: N = 100,000, K = 100 (both maximum)
n = 100000
k = 100
heights = [(i * 789 + 321) % 10000 + 1 for i in range(n)]
input_b1 = f"{n} {k}\n" + " ".join(map(str, heights))
result_b1 = run_large_test('b.py', input_b1, "N=100,000, K=100 (maximum)", timeout=15)
results.append(("Problem B - N=100K, K=100", result_b1))

# Test 2: N = 50,000, K = 50 (medium large)
n = 50000
k = 50
heights = [(i * 111 + 222) % 5000 + 1 for i in range(n)]
input_b2 = f"{n} {k}\n" + " ".join(map(str, heights))
result_b2 = run_large_test('b.py', input_b2, "N=50,000, K=50", timeout=10)
results.append(("Problem B - N=50K, K=50", result_b2))

# PROBLEM C: N ≤ 10^5
print("\n" + "="*80)
print("PROBLEM C: Vacation")
print("Constraint: N ≤ 100,000")
print("="*80)

# Test 1: N = 100,000 (maximum)
n = 100000
activities = []
for i in range(n):
    a = (i * 7 + 13) % 10000 + 1
    b = (i * 11 + 17) % 10000 + 1
    c = (i * 13 + 19) % 10000 + 1
    activities.append(f"{a} {b} {c}")
input_c1 = f"{n}\n" + "\n".join(activities)
result_c1 = run_large_test('c.py', input_c1, "N=100,000 (maximum)", timeout=5)
results.append(("Problem C - N=100K", result_c1))

# Test 2: Maximum happiness values
n = 100000
activities = ["10000 10000 10000"] * n
input_c2 = f"{n}\n" + "\n".join(activities)
result_c2 = run_large_test('c.py', input_c2, "N=100,000, all max happiness", timeout=5)
results.append(("Problem C - Max values", result_c2))

# PROBLEM D: N ≤ 100, W ≤ 10^5
print("\n" + "="*80)
print("PROBLEM D: Knapsack 1")
print("Constraint: N ≤ 100, W ≤ 100,000, v ≤ 10^9")
print("="*80)

# Test 1: N = 100, W = 100,000 (maximum)
n = 100
w = 100000
items = []
for i in range(n):
    weight = (i % 100) * 10 + 1
    value = (i + 1) * 1000000
    items.append(f"{weight} {value}")
input_d1 = f"{n} {w}\n" + "\n".join(items)
result_d1 = run_large_test('d.py', input_d1, "N=100, W=100,000 (maximum)", timeout=10)
results.append(("Problem D - N=100, W=100K", result_d1))

# Test 2: Maximum values
n = 100
w = 100000
items = [f"{i%1000+1} {1000000000}" for i in range(n)]
input_d2 = f"{n} {w}\n" + "\n".join(items)
result_d2 = run_large_test('d.py', input_d2, "N=100, W=100K, v=10^9", timeout=10)
results.append(("Problem D - Max values", result_d2))

# PROBLEM E: N ≤ 100, W ≤ 10^9
print("\n" + "="*80)
print("PROBLEM E: Knapsack 2")
print("Constraint: N ≤ 100, W ≤ 1,000,000,000, v ≤ 1000")
print("="*80)

# Test 1: Large W (10^6)
n = 100
w = 1000000
items = []
for i in range(n):
    weight = (i + 1) * 100
    value = (i + 1) * 10
    items.append(f"{weight} {value}")
input_e1 = f"{n} {w}\n" + "\n".join(items)
result_e1 = run_large_test('e.py', input_e1, "N=100, W=1,000,000", timeout=5)
results.append(("Problem E - W=10^6", result_e1))

# Test 2: Very large W (10^8)
n = 50
w = 100000000
items = []
for i in range(n):
    weight = (i + 1) * 1000000
    value = (i + 1) * 20
    items.append(f"{weight} {value}")
input_e2 = f"{n} {w}\n" + "\n".join(items)
result_e2 = run_large_test('e.py', input_e2, "N=50, W=100,000,000", timeout=5)
results.append(("Problem E - W=10^8", result_e2))

# Test 3: Maximum W (10^9) - smallest test
n = 10
w = 1000000000
items = [f"{100000000} {100}" for i in range(n)]
input_e3 = f"{n} {w}\n" + "\n".join(items)
result_e3 = run_large_test('e.py', input_e3, "N=10, W=1,000,000,000 (maximum)", timeout=5)
results.append(("Problem E - W=10^9", result_e3))

# SUMMARY
print("\n" + "="*80)
print("SUMMARY - LARGE TEST CASE RESULTS")
print("="*80)

passed = sum(1 for _, r in results if r)
total = len(results)

for name, result in results:
    status = "✅" if result else "❌"
    print(f"{status} {name}")

print(f"\n📊 Overall: {passed}/{total} large tests passed")

if passed == total:
    print("\n🎉 All large test cases passed! Your solutions scale well.")
else:
    print(f"\n⚠️  {total - passed} test(s) failed or timed out.")
    print("This indicates potential performance issues with maximum inputs.")
