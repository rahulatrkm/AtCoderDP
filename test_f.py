'''
Comprehensive stress test for Problem F - LCS (Longest Common Subsequence)
Constraints: |s|, |t| ≤ 3000
Tests edge cases, time and space complexity
'''

import subprocess
import time

def is_subsequence(subseq, string):
    """Check if subseq is a subsequence of string"""
    if not subseq:
        return True
    it = iter(string)
    return all(char in it for char in subseq)

def run_test(s, t, expected_length, description, timeout=5):
    """Run test and measure time - validates LCS length and validity"""
    # Handle empty string cases
    if not s and not t:
        input_str = "\n"
    elif not t:
        input_str = f"{s}\n"
    else:
        input_str = f"{s}\n{t}"
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'f_test.py'],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED")
            print(f"   Error: {result.stderr[:200]}")
            return False
        
        output = result.stdout.strip()
        output_len = len(output)
        
        # Check if output is valid LCS
        is_valid = (is_subsequence(output, s) and 
                   is_subsequence(output, t) and 
                   output_len == expected_length)
        
        status = "✓" if is_valid else "✗"
        time_icon = "⚡" if elapsed < 0.5 else "🐌" if elapsed > 2 else "⏱️"
        
        if is_valid:
            print(f"{status} {time_icon} {description}")
            print(f"   LCS length: {output_len} (expected: {expected_length}) [{elapsed:.3f}s]")
        else:
            print(f"{status} {time_icon} {description}")
            print(f"   Got length {output_len}, expected {expected_length}")
            if output_len > 0:
                print(f"   Valid subsequence of s: {is_subsequence(output, s)}")
                print(f"   Valid subsequence of t: {is_subsequence(output, t)}")
        return is_valid
        
    except subprocess.TimeoutExpired:
        print(f"✗ ⏰ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ ❌ {description}: ERROR - {str(e)}")
        return False

# Create test version that reads from stdin with error handling
test_code = '''
def helper(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs[::-1])

try:
    s = input().strip()
    t = input().strip()
except EOFError:
    s = ""
    t = ""
    
print(helper(s, t))
'''

with open('f_test.py', 'w') as f:
    f.write(test_code)

print("="*80)
print("PROBLEM F: LCS (Longest Common Subsequence)")
print("Constraints: |s|, |t| ≤ 3000")
print("="*80)

passed = 0
total = 0

# Sample tests
print("\n[Sample Tests]")
total += 1
passed += run_test("axyb", "abyxb", 3, "Sample 1")

# Edge cases
print("\n[Edge Cases]")
total += 1
passed += run_test("", "", 0, "Both empty")

total += 1
passed += run_test("a", "", 0, "Second empty")

total += 1
passed += run_test("", "xyz", 0, "First empty")

total += 1
passed += run_test("a", "a", 1, "Single char match")

total += 1
passed += run_test("a", "b", 0, "Single char no match")

total += 1
passed += run_test("abc", "abc", 3, "Identical strings")

total += 1
passed += run_test("abc", "xyz", 0, "No common chars")

total += 1
passed += run_test("aaa", "aaa", 3, "All same char")

total += 1
passed += run_test("abcdef", "fedcba", 1, "Reverse (any single char)")

# Boundary tests
print("\n[Boundary Tests]")
total += 1
passed += run_test("a"*100, "a"*100, 100, "100 identical chars")

total += 1
passed += run_test("abcd"*25, "dcba"*25, 49, "100 chars, overlapping pattern")

total += 1
passed += run_test("abc"*100, "xyz"*100, 0, "300 chars, no match")

# Performance tests - approaching max constraints
print("\n[Performance Tests - Time & Space]")

# Test 1: 1000x1000
s1 = "a" * 500 + "b" * 500
t1 = "b" * 500 + "a" * 500
total += 1
passed += run_test(s1, t1, 500, "1000 chars each, full overlap", timeout=3)

# Test 2: 2000x2000
s2 = "".join(chr(ord('a') + i%26) for i in range(2000))
t2 = "".join(chr(ord('a') + (i+5)%26) for i in range(2000))
# LCS length is 1995 for this pattern
total += 1
passed += run_test(s2, t2, 1995, "2000 chars, shifted pattern", timeout=5)

# Test 3: 3000x3000 (MAX)
print("\n⚠️  Maximum constraint test (may be slow):")
s3 = "".join(chr(ord('a') + i%26) for i in range(3000))
t3 = "".join(chr(ord('a') + i%26) for i in range(3000))
total += 1
passed += run_test(s3, t3, 3000, "3000x3000 identical (MAX)", timeout=10)

# Test 4: 3000x3000 no match (worst case for backtracking)
s4 = "a" * 3000
t4 = "b" * 3000
total += 1
passed += run_test(s4, t4, 0, "3000x3000 no match (worst case)", timeout=10)

# Test 5: 3000x3000 alternating pattern (LCS is actually 2999!)
s5 = "ab" * 1500
t5 = "ba" * 1500
total += 1
passed += run_test(s5, t5, 2999, "3000x3000 alternating", timeout=10)

# Summary
print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Tests Passed: {passed}/{total}")
print(f"\nComplexity Analysis:")
print(f"  Time: O(|s| × |t|) for DP + O(|s| + |t|) for backtracking")
print(f"  Space: O(|s| × |t|) for DP table")
print(f"  Max: 3000×3000 = 9M cells (manageable)")
print("="*80)

# Cleanup
import os
os.remove('f_test.py')
