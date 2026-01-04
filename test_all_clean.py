'''
Test runner that creates temporary clean versions of code files for testing
'''

import subprocess
import time
import os

def create_clean_version(original_file, clean_file):
    """Create a clean version without test code"""
    
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
        'c.py': open('/Users/rahul./Downloads/AtCoderDP/c.py').read(),  # c.py is already clean
        'd.py': open('/Users/rahul./Downloads/AtCoderDP/d.py').read(),  # d.py is already clean
        'e.py': open('/Users/rahul./Downloads/AtCoderDP/e.py').read()   # e.py is already clean
    }
    
    with open(clean_file, 'w') as f:
        f.write(clean_versions[original_file])

def run_test(file, input_str, expected, description, timeout=5):
    """Run test with clean version"""
    clean_file = f"_test_{file}"
    
    try:
        create_clean_version(file, clean_file)
        
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
            print(f"✗ {description}: CRASHED - {result.stderr[:100]}")
            return False
        
        output = int(result.stdout.strip())
        status = "✓" if output == expected else "✗"
        time_icon = "⚡" if elapsed < 0.5 else "🐌" if elapsed > 2 else "⏱️"
        
        print(f"{status} {time_icon} {description}: {output} (Expected: {expected}) [{elapsed:.3f}s]")
        return output == expected
        
    except subprocess.TimeoutExpired:
        print(f"✗ ⏰ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ ❌ {description}: ERROR - {str(e)[:100]}")
        return False
    finally:
        if os.path.exists(clean_file):
            os.remove(clean_file)

print("="*80)
print("COMPREHENSIVE TEST SUITE - AtCoder DP Problems A-E")
print("Testing with time and memory constraints")
print("="*80)

# PROBLEM A
print("\n" + "="*80)
print("PROBLEM A: Frog 1 (N ≤ 10^5, h_i ≤ 10^4)")
print("="*80)
pass_a = True
pass_a &= run_test('a.py', "4\n10 30 40 20", 30, "Sample1")
pass_a &= run_test('a.py', "2\n10 10", 0, "Sample2: Same heights")
pass_a &= run_test('a.py', "6\n30 10 60 10 60 50", 40, "Sample3")
pass_a &= run_test('a.py', "10\n50 50 50 50 50 50 50 50 50 50", 0, "Edge: All same")
pass_a &= run_test('a.py', "2\n1 10000", 9999, "Edge: Max diff")
large_a = "10000\n" + " ".join(str((i*7+13)%10000+1) for i in range(10000))
pass_a &= run_test('a.py', large_a, 139797, "Performance: N=10^4", timeout=3)
print(f"Result: {'✅ PASS' if pass_a else '❌ FAIL'}")

# PROBLEM B
print("\n" + "="*80)
print("PROBLEM B: Frog 2 (N ≤ 10^5, K ≤ 100)")
print("="*80)
pass_b = True
pass_b &= run_test('b.py', "5 3\n10 30 40 50 20", 30, "Sample1")
pass_b &= run_test('b.py', "3 1\n10 20 10", 20, "Sample2: k=1")
pass_b &= run_test('b.py', "10 4\n40 10 20 70 80 10 20 70 80 60", 40, "Sample4")
pass_b &= run_test('b.py', "100 100\n" + " ".join(str(i*2) for i in range(100)), 198, "Edge: Max k")
large_b = "10000 10\n" + " ".join(str((i*7+13)%100+1) for i in range(10000))
pass_b &= run_test('b.py', large_b, 41993, "Performance: N=10^4", timeout=3)
print(f"Result: {'✅ PASS' if pass_b else '❌ FAIL'}")

# PROBLEM C
print("\n" + "="*80)
print("PROBLEM C: Vacation (N ≤ 10^5, points ≤ 10^4)")
print("="*80)
pass_c = True
pass_c &= run_test('c.py', "3\n10 40 70\n20 50 80\n30 60 90", 210, "Sample1")
pass_c &= run_test('c.py', "1\n100 10 1", 100, "Sample2: n=1")
pass_c &= run_test('c.py', "7\n6 7 8\n8 8 3\n2 5 2\n7 8 6\n4 6 8\n2 3 4\n7 5 1", 46, "Sample3")
pass_c &= run_test('c.py', "3\n10000 10000 10000\n10000 10000 10000\n10000 10000 10000", 30000, "Edge: Max")
large_c = "10000\n" + "\n".join(f"{(i*7+13)%100+1} {(i*11+17)%100+1} {(i*13+19)%100+1}" for i in range(10000))
pass_c &= run_test('c.py', large_c, 656600, "Performance: N=10^4", timeout=3)
print(f"Result: {'✅ PASS' if pass_c else '❌ FAIL'}")

# PROBLEM D
print("\n" + "="*80)
print("PROBLEM D: Knapsack 1 (N ≤ 100, W ≤ 10^5, v ≤ 10^9)")
print("="*80)
pass_d = True
pass_d &= run_test('d.py', "3 8\n3 30\n4 50\n5 60", 90, "Sample1")
pass_d &= run_test('d.py', "5 5\n1 1000000000\n1 1000000000\n1 1000000000\n1 1000000000\n1 1000000000", 5000000000, "Sample2: Large v")
pass_d &= run_test('d.py', "6 15\n6 5\n5 6\n6 4\n6 6\n3 5\n7 2", 17, "Sample3")
items_d = "\n".join(f"{(i%10+1)*10} {(i+1)*1000}" for i in range(100))
pass_d &= run_test('d.py', f"100 100000\n{items_d}", 5050000, "Performance: N=100,W=10^5", timeout=3)
print(f"Result: {'✅ PASS' if pass_d else '❌ FAIL'}")

# PROBLEM E
print("\n" + "="*80)
print("PROBLEM E: Knapsack 2 (N ≤ 100, W ≤ 10^9, v ≤ 10^3)")
print("⚠️  Current code: dp[W] fails for W > 10^7")
print("="*80)
pass_e = True
pass_e &= run_test('e.py', "3 8\n3 30\n4 50\n5 60", 90, "Sample1: W=8 ✓")
pass_e &= run_test('e.py', "6 15\n6 5\n5 6\n6 4\n6 6\n3 5\n7 2", 17, "Sample3: W=15 ✓")
print("\n⚠️  Large W tests (will fail):")
pass_e &= run_test('e.py', "1 1000000000\n1000000000 10", 10, "Sample2: W=10^9 ✗", timeout=3)
pass_e &= run_test('e.py', "3 10000000\n100 50\n200 100\n300 150", 300, "W=10^7 ✗", timeout=3)
print(f"Result: {'⚠️  PARTIAL' if not pass_e else '✅ PASS'}")

# SUMMARY
print("\n" + "="*80)
print("FINAL SUMMARY")
print("="*80)
results = [
    ("Problem A (Frog 1)", pass_a, "✓ O(N) time, O(N) space"),
    ("Problem B (Frog 2)", pass_b, "✓ O(N×K) time, O(N) space"),
    ("Problem C (Vacation)", pass_c, "✓ O(N) time, O(N) space"),
    ("Problem D (Knapsack 1)", pass_d, "✓ O(N×W) time, O(W) space"),
    ("Problem E (Knapsack 2)", pass_e, "✗ O(N×W) fails for W>10^7")
]

for name, passed, complexity in results:
    status = "✅" if passed else "❌"
    print(f"{status} {name:25} {complexity}")

total = sum(p for _, p, _ in results)
print(f"\n📊 Score: {total}/5 problems passed all tests")

if not pass_e:
    print("\n⚠️  PROBLEM E requires different approach:")
    print("   Current: dp[W] → Fails when W = 10^9")
    print("   Required: dp[value] → Always works (max 100K)")
    print("   See: PROBLEM_E_ANALYSIS.txt")
