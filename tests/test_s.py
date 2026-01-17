"""
Test cases for Problem S: Digit Sum
https://atcoder.jp/contests/dp/tasks/dp_s
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "30\n4", "6"),
    TestCase("Sample 2", "1000000009\n1", "2"),
    TestCase("Sample 3", "98765432109876543210\n58", "635270834"),
    
    # Edge Cases
    TestCase("K=9 D=3", "9\n3", "3"),
    TestCase("K=100 D=10", "100\n10", "9"),
]

if __name__ == "__main__":
    run_tests("s", TEST_CASES)
