'''
Stress test for Problem E with maximum constraints
Tests the limits of recursive memoization approach
'''

import subprocess
import time

def run_test(input_str, description, timeout=10):
    """Run test and measure time/memory"""
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'e.py'],
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
        status = "✓" if elapsed < 3 else "⚠️"
        print(f"{status} {description}")
        print(f"   Result: {output}, Time: {elapsed:.3f}s")
        return True
        
    except subprocess.TimeoutExpired:
        print(f"✗ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ {description}: ERROR - {str(e)}")
        return False

print("="*80)
print("STRESS TESTING Problem E - Recursive Memoization Limits")
print("="*80)

# Test 1: Maximum N with diverse weights
print("\n[Test 1] N=100, diverse weights (many states)")
items1 = "\n".join(f"{i+1} {i+1}" for i in range(100))
run_test(f"100 5000\n{items1}", "N=100, W=5000, diverse weights", timeout=5)

# Test 2: Maximum N with W approaching 10^6
print("\n[Test 2] N=100, W=10^6")
items2 = "\n".join(f"{(i%50+1)*1000} {i+1}" for i in range(100))
run_test(f"100 1000000\n{items2}", "N=100, W=10^6, large W", timeout=5)

# Test 3: All items with weight=1, W=100K (triggers 100K states)
print("\n[Test 3] N=100, all weight=1, W=100,000")
items3 = "\n".join("1 10" for _ in range(100))
run_test(f"100 100000\n{items3}", "Worst case: 100*100K states", timeout=5)

# Test 4: Maximum values
print("\n[Test 4] N=100, max values (v=1000)")
items4 = "\n".join(f"{(i%10+1)*100} 1000" for i in range(100))
run_test(f"100 10000\n{items4}", "N=100, max values, W=10K", timeout=5)

# Test 5: Extreme W with sparse weights
print("\n[Test 5] W=10^9 with sparse weights (few states)")
items5 = "\n".join(f"{10**8} {i+1}" for i in range(10))
run_test(f"10 1000000000\n{items5}", "W=10^9, sparse (10 items)", timeout=5)

# Test 6: W=10^9 with small weights (many states)
print("\n[Test 6] W=10^9 with small weights (DANGER)")
items6 = "\n".join(f"{i+1} {i+1}" for i in range(100))
run_test(f"100 1000000000\n{items6}", "W=10^9, small weights (DANGER)", timeout=10)

print("\n" + "="*80)
print("CONCLUSION:")
print("✓ Recursive memoization works when: few reachable states")
print("✗ Fails when: many items with small weights + large W")
print("  → States = O(N * reachable_W) can be huge")
print("="*80)
