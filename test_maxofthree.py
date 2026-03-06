from module import max_of_three
FUNCTION_TO_TEST = max_of_three

TESTS = [
    ((1, 2, 3), 3),
    ((10, 5, 8), 10),
    ((-1, -5, -3), -1),
    ((7, 7, 7), 7),
]

# ==========================================
# 🚫 DO NOT EDIT BELOW THIS LINE
# ==========================================

import sys
from os import system
system("clear")

def run_all_tests():
    one_or_more_failures = False

    for i, (inputs, expected) in enumerate(TESTS):
        if one_test_success(inputs, expected):
            print(f"Test {i}: Pass!")
        else:
            print(f"Test {i}: Fail")
            one_or_more_failures = True
        print()

    print("\n-------------------------")

    if one_or_more_failures:
        print("❌ One or more tests failed.")
    else:
        print("✅ All tests passed!")


def one_test_success(inputs, expected):
    try:
        actual = FUNCTION_TO_TEST(*inputs)
        print(f"Expected: {expected}, Got: {actual}")
        assert actual == expected
        return True
    except Exception as e:
        # print(f"Error: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)