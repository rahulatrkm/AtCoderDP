"""
Test cases for Problem A: Frog 1
https://atcoder.jp/contests/dp/tasks/dp_a
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4\n10 30 40 20", "30"),
    TestCase("Sample 2", "2\n10 10", "0"),
    TestCase("Sample 3", "6\n30 10 60 10 60 50", "40"),
    
    # Edge Cases
    TestCase("Min N=2", "2\n1 100", "99"),
    TestCase("All same height", "5\n50 50 50 50 50", "0"),
    TestCase("Increasing", "5\n1 2 3 4 5", "4"),
    TestCase("Decreasing", "5\n5 4 3 2 1", "4"),
    TestCase("Skip better", "4\n10 100 20 30", "20"),  # 10->20->30 = 10+10=20
    TestCase("Large diff", "3\n1 10000 1", "0"),       # 1->1 via skip = 0
    TestCase("Zigzag", "5\n1 100 1 100 1", "0"),
]

if __name__ == "__main__":
    run_tests("a", TEST_CASES)
