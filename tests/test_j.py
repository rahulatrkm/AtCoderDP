"""
Test cases for Problem J: Sushi
https://atcoder.jp/contests/dp/tasks/dp_j
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3\n1 1 1", "5.5"),
    TestCase("Sample 2", "1\n3", "3"),
    TestCase("Sample 3", "2\n1 2", "4.5"),
    
    # Edge Cases
    TestCase("Single plate 1", "1\n1", "1.0"),
    TestCase("All zeros", "3\n0 0 0", "0.0"),
    TestCase("All ones", "2\n1 1", "3.0"),
]

if __name__ == "__main__":
    run_tests("j", TEST_CASES)
