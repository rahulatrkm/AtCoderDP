'''
Comprehensive test for Problem J - Sushi
Constraints: N ≤ 300, count plates with 1, 2, or 3 sushi
Calculate expected number of operations to empty all plates
Tests edge cases, time and space complexity
'''

import subprocess
import time

def run_test(n, plates, expected, description, timeout=10):
    """Run test and measure time"""
    input_str = f"{n}\n"
    input_str += " ".join(map(str, plates))
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'j.py'],
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
        
        output = float(result.stdout.strip())
        # Allow small floating point error
        passed = abs(output - expected) < 0.001
        status = "✓" if passed else "✗"
        time_icon = "⚡" if elapsed < 0.5 else "🐌" if elapsed > 2 else "⏱️"
        
        print(f"{status} {time_icon} {description}")
        print(f"   Result: {output:.6f} (Expected: {expected:.6f}) [{elapsed:.3f}s]")
        return passed
        
    except subprocess.TimeoutExpired:
        print(f"✗ ⏰ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ ❌ {description}: ERROR - {str(e)}")
        return False

print("="*80)
print("PROBLEM J: Sushi (Expected operations to empty plates)")
print("Constraints: N ≤ 300, plates have 0-3 sushi")
print("="*80)

passed = 0
total = 0

# Sample tests
print("\n[Sample Tests]")
total += 1
passed += run_test(3, [1, 1, 1], 5.5, "Sample 1: three plates with 1 sushi")

total += 1
passed += run_test(1, [3], 3.0, "Sample 2: one plate with 3 sushi")

total += 1
passed += run_test(2, [1, 2], 4.5, "Sample 3: mixed 1 and 2 sushi")

# Edge cases
print("\n[Edge Cases]")
total += 1
passed += run_test(1, [1], 1.0, "Single plate, 1 sushi")

total += 1
passed += run_test(1, [2], 2.0, "Single plate, 2 sushi")

total += 1
passed += run_test(2, [2, 2], 5.5, "Two plates, 2 sushi each")

total += 1
passed += run_test(3, [3, 3, 3], 13.486883, "Three plates, 3 sushi each")

total += 1
passed += run_test(5, [0, 0, 0, 1, 1], 7.5, "Some empty plates")

# Small tests with various configurations
print("\n[Small Configuration Tests]")
total += 1
passed += run_test(2, [1, 3], 6.25, "Two plates: 1 and 3")

total += 1
passed += run_test(3, [1, 2, 3], 10.548611, "Three plates: 1, 2, 3")

total += 1
passed += run_test(4, [1, 1, 1, 1], 8.333333, "Four plates: all 1s")

total += 1
passed += run_test(5, [2, 2, 2, 2, 2], 19.041361, "Five plates: all 2s")

# Larger tests
print("\n[Medium Size Tests]")
total += 1
plates_10 = [1] * 10
passed += run_test(10, plates_10, 29.289683, "10 plates: all 1s", timeout=5)

# Larger tests
print("\n[Medium Size Tests]")
total += 1
plates_10 = [1] * 10
passed += run_test(10, plates_10, 29.289683, "10 plates: all 1s", timeout=5)

total += 1
plates_10_small = [1, 2, 3, 1, 2]
passed += run_test(5, plates_10_small, 19.287831, "5 plates: small mixed", timeout=5)

# Performance note
print("\n[Performance Analysis]")
print("⚠️  WARNING: Current algorithm has exponential state space!")
print("   - State = tuple of all plate values")
print("   - For N plates, this creates N! / (k1! × k2! × k3!) states")
print("   - N=20+ causes exponential blowup")
print("   - Proper solution: State should be (c1, c2, c3) only")
print("   - Where c1=#plates with 1, c2=#plates with 2, c3=#plates with 3")

# Test only small cases to avoid timeout
print("\n[Small Tests Only - Large N would timeout]")
total += 1
plates_15 = [1] * 15
result_15 = "Skipped - would timeout"
print(f"⚠️  15 plates: {result_15}")

total += 1
plates_20 = [1] * 20
result_20 = "Skipped - would timeout"
print(f"⚠️  20 plates: {result_20}")

# Summary
print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Tests Passed: {passed}/{total}")
print(f"\nComplexity Analysis:")
print(f"  ⚠️  CRITICAL ISSUE: Current implementation uses wrong state representation!")
print(f"  Current: State = tuple of all plate values → Exponential states")
print(f"  Correct: State = (c1, c2, c3) where ci = count of plates with i sushi")
print(f"  ")
print(f"  Current Complexity:")
print(f"    States: Exponential - all permutations of plate values")
print(f"    Time: Exponential - cannot handle N > 15")
print(f"    Space: Exponential - cache explodes")
print(f"  ")
print(f"  Optimal Complexity (with correct state):")
print(f"    States: O(N^3) - only (c1, c2, c3) where c1+c2+c3 ≤ N")
print(f"    Time: O(N^3) - manageable for N=300")
print(f"    Space: O(N^3) - ~27M states for N=300")
print(f"  ")
print(f"  Conclusion: Algorithm works correctly for small N (≤10)")
print(f"             But fails for larger N due to wrong state representation")
print("="*80)
