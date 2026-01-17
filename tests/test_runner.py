"""
Test runner for AtCoder DP solutions.
Runs each solution with test cases and validates output.
"""

import subprocess
import sys
import os
from pathlib import Path

# Get project root
PROJECT_ROOT = Path(__file__).parent.parent

def run_solution(problem: str, input_data: str, timeout: float = 5.0, multiline: bool = False) -> tuple[int, str, str]:
    """
    Run a solution file with given input.
    Returns (return_code, stdout, stderr)
    If multiline=False, only returns the FIRST line of output.
    If multiline=True, returns all lines.
    """
    solution_file = PROJECT_ROOT / f"{problem}.py"
    
    try:
        result = subprocess.run(
            [sys.executable, str(solution_file)],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=PROJECT_ROOT
        )
        if multiline:
            return result.returncode, result.stdout.strip(), result.stderr
        else:
            # Only take the first line of output (the actual answer)
            first_line = result.stdout.strip().split('\n')[0] if result.stdout.strip() else ""
            return result.returncode, first_line, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)


def check_output(actual: str, expected: str, float_tolerance: float = 1e-6) -> bool:
    """Compare actual output with expected output. Handles floats with tolerance."""
    actual = actual.strip()
    expected = expected.strip()
    
    # First try exact match
    if actual == expected:
        return True
    
    # Try float comparison
    try:
        actual_f = float(actual)
        expected_f = float(expected)
        return abs(actual_f - expected_f) < float_tolerance
    except ValueError:
        pass
    
    return False


class TestCase:
    def __init__(self, name: str, input_data: str, expected: str, multiline: bool = False):
        self.name = name
        self.input_data = input_data
        self.expected = expected
        self.multiline = multiline


def run_tests(problem: str, test_cases: list[TestCase], verbose: bool = True) -> tuple[int, int]:
    """
    Run all test cases for a problem.
    Returns (passed, total)
    """
    passed = 0
    total = len(test_cases)
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"Testing Problem {problem.upper()}")
        print(f"{'='*60}")
    
    for tc in test_cases:
        ret_code, stdout, stderr = run_solution(problem, tc.input_data, multiline=tc.multiline)
        
        if ret_code == -1:
            status = f"✗ ERROR: {stderr[:50]}"
        elif check_output(stdout, tc.expected):
            status = "✓ PASS"
            passed += 1
        else:
            # Truncate output for display
            display_out = stdout.replace('\n', '\\n')[:30]
            display_exp = tc.expected.replace('\n', '\\n')[:30]
            status = f"✗ FAIL: got '{display_out}', expected '{display_exp}'"
        
        if verbose:
            print(f"  {tc.name}: {status}")
    
    if verbose:
        print(f"\nResult: {passed}/{total} passed")
    
    return passed, total
