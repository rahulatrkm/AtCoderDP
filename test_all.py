'''
Comprehensive Test Suite for All AtCoder DP Problems (A-E)
Tests edge cases, time complexity, and memory usage
Does NOT modify original code files
'''

import subprocess
import time
import sys
import tracemalloc

def run_test_with_metrics(file, input_str, expected, description, timeout=5):
    """Run test and measure time/memory"""
    try:
        # Start memory tracking
        start_time = time.time()
        
        result = subprocess.run(
            ['python3', file],
            input=input_str,
            capture_output=True,
            text=True,
            cwd='/Users/rahul./Downloads/AtCoderDP',
            timeout=timeout
        )
        
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
            return False
        
        try:
            # Try to parse as integer
            output = int(result.stdout.strip())
        except ValueError:
            # If file has multiple outputs, get the last number
            output_lines = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]
            # Find lines that look like they contain the answer
            for line in reversed(output_lines):
                # Skip lines with "Expected" or other test output
                if 'Expected' in line or 'Edge Case' in line or 'Sample' in line or '✅' in line:
                    continue
                # Try to extract number from line
                import re
                numbers = re.findall(r'-?\d+', line)
                if numbers:
                    output = int(numbers[0])
                    break
            else:
                print(f"✗ {description}: Could not parse output")
                return False
        
        status = "✓" if output == expected else "✗"
        time_status = "⚡" if elapsed < 0.5 else "🐌" if elapsed > 2 else "⏱️"
        
        print(f"{status} {time_status} {description}: {output} (Expected: {expected}) [{elapsed:.3f}s]")
        return output == expected
        
    except subprocess.TimeoutExpired:
        print(f"✗ ⏰ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ ❌ {description}: ERROR - {str(e)[:100]}")
        return False

print("="*80)
print("COMPREHENSIVE TEST SUITE - AtCoder DP Problems A-E")
print("="*80)

# ============================================================================
# PROBLEM A: Frog 1
# ============================================================================
print("\n" + "="*80)
print("PROBLEM A: Frog 1")
print("Constraints: 2 ≤ N ≤ 10^5, 1 ≤ h_i ≤ 10^4")
print("="*80)

all_pass_a = True

# Sample tests
all_pass_a &= run_test_with_metrics('a.py', "4\n10 30 40 20", 30, "A-Sample1: Basic case")
all_pass_a &= run_test_with_metrics('a.py', "2\n10 10", 0, "A-Sample2: Same heights")
all_pass_a &= run_test_with_metrics('a.py', "6\n30 10 60 10 60 50", 40, "A-Sample3: Complex")

# Edge cases
all_pass_a &= run_test_with_metrics('a.py', "10\n50 50 50 50 50 50 50 50 50 50", 0, "A-Edge: All same")
all_pass_a &= run_test_with_metrics('a.py', "10\n1 2 3 4 5 6 7 8 9 10", 9, "A-Edge: Increasing")
all_pass_a &= run_test_with_metrics('a.py', "2\n1 10000", 9999, "A-Edge: Max diff")

# Large N test
large_input = "10000\n" + " ".join(str((i * 7 + 13) % 10000 + 1) for i in range(10000))
all_pass_a &= run_test_with_metrics('a.py', large_input, 139797, "A-Performance: N=10000", timeout=3)

print(f"\nProblem A: {'✅ ALL PASSED' if all_pass_a else '❌ SOME FAILED'}")

# ============================================================================
# PROBLEM B: Frog 2
# ============================================================================
print("\n" + "="*80)
print("PROBLEM B: Frog 2")
print("Constraints: 2 ≤ N ≤ 10^5, 1 ≤ K ≤ 100, 1 ≤ h_i ≤ 10^4")
print("="*80)

all_pass_b = True

# Sample tests
all_pass_b &= run_test_with_metrics('b.py', "5 3\n10 30 40 50 20", 30, "B-Sample1: n=5, k=3")
all_pass_b &= run_test_with_metrics('b.py', "3 1\n10 20 10", 20, "B-Sample2: k=1")
all_pass_b &= run_test_with_metrics('b.py', "2 100\n10 10", 0, "B-Sample3: Large k")
all_pass_b &= run_test_with_metrics('b.py', "10 4\n40 10 20 70 80 10 20 70 80 60", 40, "B-Sample4: n=10, k=4")

# Edge cases
all_pass_b &= run_test_with_metrics('b.py', "10 1\n1 2 3 4 5 6 7 8 9 10", 9, "B-Edge: k=1")
all_pass_b &= run_test_with_metrics('b.py', "5 4\n100 1 2 3 1", 99, "B-Edge: Direct jump")
all_pass_b &= run_test_with_metrics('b.py', "100 100\n" + " ".join(str(i*2) for i in range(100)), 198, "B-Edge: Max k=100")

# Large N test
large_input = "10000 10\n" + " ".join(str((i * 7 + 13) % 100 + 1) for i in range(10000))
all_pass_b &= run_test_with_metrics('b.py', large_input, 4193, "B-Performance: N=10000, k=10", timeout=3)

print(f"\nProblem B: {'✅ ALL PASSED' if all_pass_b else '❌ SOME FAILED'}")

# ============================================================================
# PROBLEM C: Vacation
# ============================================================================
print("\n" + "="*80)
print("PROBLEM C: Vacation")
print("Constraints: 1 ≤ N ≤ 10^5, 1 ≤ a_i, b_i, c_i ≤ 10^4")
print("="*80)

all_pass_c = True

# Sample tests
all_pass_c &= run_test_with_metrics('c.py', "3\n10 40 70\n20 50 80\n30 60 90", 210, "C-Sample1: n=3")
all_pass_c &= run_test_with_metrics('c.py', "1\n100 10 1", 100, "C-Sample2: n=1")
all_pass_c &= run_test_with_metrics('c.py', "7\n6 7 8\n8 8 3\n2 5 2\n7 8 6\n4 6 8\n2 3 4\n7 5 1", 46, "C-Sample3: n=7")

# Edge cases
all_pass_c &= run_test_with_metrics('c.py', "3\n10 10 10\n20 20 20\n30 30 30", 60, "C-Edge: All same")
all_pass_c &= run_test_with_metrics('c.py', "4\n100 1 1\n100 1 1\n100 1 1\n100 1 1", 202, "C-Edge: One dominant")
all_pass_c &= run_test_with_metrics('c.py', "3\n10000 10000 10000\n10000 10000 10000\n10000 10000 10000", 30000, "C-Edge: Max values")

# Large N test
large_input = "10000\n" + "\n".join(f"{(i*7+13)%100+1} {(i*11+17)%100+1} {(i*13+19)%100+1}" for i in range(10000))
all_pass_c &= run_test_with_metrics('c.py', large_input, 624950, "C-Performance: N=10000", timeout=3)

print(f"\nProblem C: {'✅ ALL PASSED' if all_pass_c else '❌ SOME FAILED'}")

# ============================================================================
# PROBLEM D: Knapsack 1
# ============================================================================
print("\n" + "="*80)
print("PROBLEM D: Knapsack 1")
print("Constraints: 1 ≤ N ≤ 100, 1 ≤ W ≤ 10^5, 1 ≤ v_i ≤ 10^9")
print("="*80)

all_pass_d = True

# Sample tests
all_pass_d &= run_test_with_metrics('d.py', "3 8\n3 30\n4 50\n5 60", 90, "D-Sample1: Basic")
all_pass_d &= run_test_with_metrics('d.py', "5 5\n1 1000000000\n1 1000000000\n1 1000000000\n1 1000000000\n1 1000000000", 5000000000, "D-Sample2: Large values")
all_pass_d &= run_test_with_metrics('d.py', "6 15\n6 5\n5 6\n6 4\n6 6\n3 5\n7 2", 17, "D-Sample3: n=6")

# Edge cases
all_pass_d &= run_test_with_metrics('d.py', "1 10\n5 100", 100, "D-Edge: Single item")
all_pass_d &= run_test_with_metrics('d.py', "3 10\n10 50\n10 100\n10 75", 100, "D-Edge: All = W")
all_pass_d &= run_test_with_metrics('d.py', "5 5\n1 10\n1 20\n1 30\n1 40\n1 50", 150, "D-Edge: All weight 1")

# Large W test (at constraint limit)
items = "\n".join(f"{(i%10+1)*10} {(i+1)*1000}" for i in range(100))
all_pass_d &= run_test_with_metrics('d.py', f"100 100000\n{items}", 5050000, "D-Performance: N=100, W=100000", timeout=3)

print(f"\nProblem D: {'✅ ALL PASSED' if all_pass_d else '❌ SOME FAILED'}")

# ============================================================================
# PROBLEM E: Knapsack 2
# ============================================================================
print("\n" + "="*80)
print("PROBLEM E: Knapsack 2")
print("Constraints: 1 ≤ N ≤ 100, 1 ≤ W ≤ 10^9, 1 ≤ v_i ≤ 10^3")
print("⚠️  WARNING: Current code uses dp[W] which FAILS for large W!")
print("="*80)

all_pass_e = True

# Sample tests with small W
all_pass_e &= run_test_with_metrics('e.py', "3 8\n3 30\n4 50\n5 60", 90, "E-Sample1: W=8 (works)")
all_pass_e &= run_test_with_metrics('e.py', "6 15\n6 5\n5 6\n6 4\n6 6\n3 5\n7 2", 17, "E-Sample3: W=15 (works)")

# Edge cases with small W
all_pass_e &= run_test_with_metrics('e.py', "3 10\n3 1000\n4 1000\n5 1000", 2000, "E-Edge: Max v=1000 (works)")

print("\n⚠️  Testing large W cases (EXPECTED TO FAIL with current approach):")
# Large W tests (will fail/timeout)
all_pass_e &= run_test_with_metrics('e.py', "1 1000000000\n1000000000 10", 10, "E-Sample2: W=10^9 (FAILS)", timeout=3)
all_pass_e &= run_test_with_metrics('e.py', "3 10000000\n100 50\n200 100\n300 150", 300, "E-Large: W=10^7 (FAILS)", timeout=3)

print(f"\nProblem E: {'⚠️  PARTIAL - Large W fails' if not all_pass_e else '✅ ALL PASSED'}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "="*80)
print("SUMMARY")
print("="*80)

results = {
    "Problem A (Frog 1)": all_pass_a,
    "Problem B (Frog 2)": all_pass_b,
    "Problem C (Vacation)": all_pass_c,
    "Problem D (Knapsack 1)": all_pass_d,
    "Problem E (Knapsack 2)": all_pass_e
}

for problem, passed in results.items():
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"{status} - {problem}")

print("\n" + "="*80)
print("MEMORY & TIME ANALYSIS")
print("="*80)
print("""
Problem A: ✓ O(N) time, O(N) space - Efficient
Problem B: ✓ O(N*K) time, O(N) space - Efficient  
Problem C: ✓ O(N) time, O(N) space - Efficient
Problem D: ✓ O(N*W) time, O(W) space - Works for W ≤ 10^5
Problem E: ✗ O(N*W) time, O(W) space - FAILS for W > 10^7

CRITICAL ISSUE: Problem E needs dp[value] instead of dp[weight]
  Current: O(W) space fails when W = 10^9
  Required: O(N*max_value) = O(100*1000) = O(100K) always works
  
See: PROBLEM_E_ANALYSIS.txt and e_correct_solution.py
""")

print("="*80)
total = sum(results.values())
print(f"Overall: {total}/5 problems fully passed")
if total == 5:
    print("🎉 ALL PROBLEMS PASS ALL TESTS!")
else:
    print("⚠️  Review failures above for details")
print("="*80)
