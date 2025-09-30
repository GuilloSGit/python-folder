class Solution:
    def count_distinct_characters(self, s: str) -> int:
        """Return the number of distinct characters in the string ``s``."""
        print(f"Distinct characters in {s!r}: {set(s)!r}")
        return len(set(s))


def main():
    """Test the solution with provided examples"""
    solution = Solution()

    # Test cases: (input string, expected distinct count)
    test_cases = [
        ("hello", 4),
        ("AaBbA", 4),
        ("", 0),
        ("  ", 1),
    ]

    for i, (text, expected) in enumerate(test_cases, 1):
        result = solution.count_distinct_characters(text)
        print(f"Test case {i}: s={text!r}")
        print(f"Result: {result}")

        # Verify the result
        if result == expected:
            print("✓ Correct!")
        else:
            print(f"✗ Expected {expected}")
        print()


if __name__ == "__main__":
    main()
