"""
Test cases for Problem K: Stones
https://atcoder.jp/contests/dp/tasks/dp_k
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "2 4\n2 3", "First"),
    TestCase("Sample 2", "2 5\n2 3", "Second"),
    TestCase("Sample 3", "2 7\n2 3", "First"),
    TestCase("Sample 4", "3 20\n1 2 3", "Second"),
    TestCase("Sample 5", "3 21\n1 2 3", "First"),
    TestCase("Sample 6", "1 100000\n1", "Second"),
    
    # Edge Cases
    TestCase("K=1, a=[1]", "1 1\n1", "First"),
    TestCase("K=0 (impossible)", "1 0\n1", "Second"),
]

if __name__ == "__main__":
    run_tests("k", TEST_CASES)
