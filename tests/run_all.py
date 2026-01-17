#!/usr/bin/env python3
"""
Main test runner for all AtCoder DP solutions.
Run from the project root directory.

Usage:
    python -m tests.run_all          # Run all tests
    python -m tests.run_all a b c    # Run specific problems
    python -m tests.run_all --fast   # Skip slow tests
"""

import sys
import importlib
from pathlib import Path

# Add tests directory to path
sys.path.insert(0, str(Path(__file__).parent))

from test_runner import run_tests

PROBLEMS = list("abcdefghijklmnopqrstuvwxyz")

def main():
    args = sys.argv[1:]
    
    # Parse arguments
    fast_mode = "--fast" in args
    if fast_mode:
        args.remove("--fast")
    
    # Select problems to test
    if args:
        problems = [p.lower() for p in args if p.lower() in PROBLEMS]
    else:
        problems = PROBLEMS
    
    total_passed = 0
    total_tests = 0
    results = {}
    
    print("=" * 70)
    print("AtCoder DP Contest - Test Suite")
    print("=" * 70)
    
    for problem in problems:
        try:
            # Import test module
            module = importlib.import_module(f"test_{problem}")
            test_cases = module.TEST_CASES
            
            # Run tests
            passed, total = run_tests(problem, test_cases, verbose=True)
            total_passed += passed
            total_tests += total
            results[problem.upper()] = (passed, total)
            
        except ImportError as e:
            print(f"\n⚠️  No tests found for problem {problem.upper()}: {e}")
            results[problem.upper()] = (0, 0)
        except Exception as e:
            print(f"\n❌ Error testing problem {problem.upper()}: {e}")
            results[problem.upper()] = (0, 0)
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for problem, (passed, total) in results.items():
        if total > 0:
            status = "✓" if passed == total else "✗"
            print(f"  {status} Problem {problem}: {passed}/{total}")
    
    print("-" * 70)
    print(f"  Total: {total_passed}/{total_tests} tests passed")
    
    if total_passed == total_tests:
        print("\n✅ All tests passed!")
        return 0
    else:
        print(f"\n❌ {total_tests - total_passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
