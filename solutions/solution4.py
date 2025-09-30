from typing import List


class Solution:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        """Return the length of the smallest contiguous subarray with sum >= target."""
        n = len(nums)
        left = 0
        total = 0
        min_len = float("inf")

        for right in range(n):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len


def main() -> None:
    """Test the solution with provided examples."""
    solution = Solution()

    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),  # [4,3]
        (4, [1, 4, 4], 1),          # [4]
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),  # no subarray
    ]

    for i, (target, nums, expected) in enumerate(test_cases, 1):
        result = solution.min_sub_array_len(target, nums)
        print(f"Test case {i}: target={target}, nums={nums}")
        print(f"Result: {result}")

        if result == expected:
            print("✓ Correct!")
        else:
            print(f"✗ Incorrect, expected {expected}")
        print()


if __name__ == "__main__":
    main()
