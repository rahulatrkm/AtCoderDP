"""
Test cases for Problem T: Permutation
https://atcoder.jp/contests/dp/tasks/dp_t
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4\n<><", "5"),
    TestCase("Sample 2", "5\n<<<<", "1"),
    TestCase("Sample 3", "20\n>>>><>>><>><>>><<>>", "217136290"),
    
    # Edge Cases
    TestCase("All <", "3\n<<", "1"),
    TestCase("All >", "3\n>>", "1"),
    TestCase("N=2 <", "2\n<", "1"),
    TestCase("N=2 >", "2\n>", "1"),
]

if __name__ == "__main__":
    run_tests("t", TEST_CASES)
