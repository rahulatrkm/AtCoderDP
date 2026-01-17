"""
Test cases for Problem C: Vacation
https://atcoder.jp/contests/dp/tasks/dp_c
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3\n10 40 70\n20 50 80\n30 60 90", "210"),
    TestCase("Sample 2", "1\n100 10 1", "100"),
    TestCase("Sample 3", "7\n6 7 8\n8 8 3\n2 5 2\n7 8 6\n4 6 8\n2 3 4\n7 5 1", "46"),
    
    # Edge Cases
    TestCase("N=1 pick max", "1\n1 2 3", "3"),
    TestCase("All same", "3\n10 10 10\n10 10 10\n10 10 10", "30"),
    TestCase("Force alternation", "2\n100 1 1\n1 1 100", "200"),
    TestCase("Greedy fails", "3\n100 1 1\n1 50 1\n1 1 100", "250"),
]

if __name__ == "__main__":
    run_tests("c", TEST_CASES)
