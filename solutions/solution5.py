from typing import List


class Solution:
    def min_column_insertions(self, matrix: List[List[int]]) -> int:
        """Return the minimum number of columns needed to make every row a palindrome."""

        def min_insertions_to_palindrome(arr: List[int]) -> int:
            n = len(arr)
            # dp[i][j] = longitud del LPS en arr[i:j+1]
            dp = [[0] * n for _ in range(n)]

            for i in range(n - 1, -1, -1):
                dp[i][i] = 1
                for j in range(i + 1, n):
                    if arr[i] == arr[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

            lps = dp[0][n - 1]
            return n - lps  # inserciones mínimas

        if not matrix:
            return 0

        return max(min_insertions_to_palindrome(row) for row in matrix)


def main() -> None:
    """Test the solution with provided examples."""
    solution = Solution()

    test_cases = [
        (
            [[0, 1, 0], [1, 0, 1]],
            0,
        ),
        (
            [[0, 1, 1], [1, 0, 0]],
            1,
        ),
        (
            [[1, 0, 1, 1], [1, 1, 0, 0]],
            2,
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = solution.min_column_insertions(matrix)
        print(f"Test case {i}: matrix={matrix}")
        print(f"Result: {result}")

        if result == expected:
            print("✓ Correct!")
        else:
            print(f"✗ Incorrect, expected {expected}")
        print()


if __name__ == "__main__":
    main()
