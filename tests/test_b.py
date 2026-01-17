"""
Test cases for Problem B: Frog 2
https://atcoder.jp/contests/dp/tasks/dp_b
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "5 3\n10 30 40 50 20", "30"),
    TestCase("Sample 2", "3 1\n10 20 10", "20"),
    TestCase("Sample 3", "2 100\n10 10", "0"),
    TestCase("Sample 4", "10 4\n40 10 20 70 80 10 20 70 80 60", "40"),
    
    # Edge Cases
    TestCase("K=1 only", "4 1\n1 2 3 4", "3"),
    TestCase("K=N-1", "5 4\n10 20 30 40 5", "5"),
    TestCase("All same", "5 3\n50 50 50 50 50", "0"),
    TestCase("Large K", "3 100\n1 1000 2", "1"),
]

if __name__ == "__main__":
    run_tests("b", TEST_CASES)
