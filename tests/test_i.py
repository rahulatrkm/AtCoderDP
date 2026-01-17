"""
Test cases for Problem I: Coins
https://atcoder.jp/contests/dp/tasks/dp_i
"""

from test_runner import TestCase, run_tests

def check_float(actual: str, expected: str, tolerance: float = 1e-9) -> bool:
    try:
        return abs(float(actual) - float(expected)) < tolerance
    except:
        return False

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3\n0.30 0.60 0.80", "0.612"),
    TestCase("Sample 2", "1\n0.50", "0.5"),
    TestCase("Sample 3", "5\n0.42 0.01 0.42 0.99 0.42", "0.3821815872"),
    
    # Edge Cases
    TestCase("All heads", "3\n1.0 1.0 1.0", "1.0"),
    TestCase("All tails", "3\n0.0 0.0 0.0", "0.0"),
    TestCase("Even coins 50-50", "2\n0.5 0.5", "0.25"),
]

if __name__ == "__main__":
    run_tests("i", TEST_CASES)
