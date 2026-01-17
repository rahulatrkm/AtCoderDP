"""
Test cases for Problem F: LCS
https://atcoder.jp/contests/dp/tasks/dp_f
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "axyb\nabyxb", "axb"),
    TestCase("Sample 2", "aa\nxayaz", "aa"),
    TestCase("Sample 3", "a\nz", ""),
    TestCase("Sample 4", "abracadabra\navadakedavra", "aaadara"),
    
    # Edge Cases
    TestCase("Identical", "abc\nabc", "abc"),
    TestCase("No match", "abc\nxyz", ""),
    TestCase("Single char match", "a\na", "a"),
    TestCase("Subsequence", "ace\nabcde", "ace"),
]

if __name__ == "__main__":
    run_tests("f", TEST_CASES)
