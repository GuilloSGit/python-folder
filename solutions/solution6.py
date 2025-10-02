from typing import List


class Solution:
    def sort_binary_rows(self, matrix: List[List[int]]) -> List[List[int]]:
        """Return a matrix where every row is sorted in non-decreasing order."""
        result = []
        for row in matrix:
            # Contar el número de 0s
            num_zeros = sum(1 for x in row if x == 0)
            # Construir la fila: num_zeros veces 0, y el resto 1s
            sorted_row = [0] * num_zeros + [1] * (len(row) - num_zeros)
            result.append(sorted_row)
        return result


def main() -> None:
    """Test the solution with provided examples."""
    solution = Solution()

    test_cases = [
        (
            [[1, 0, 1], [0, 1, 1]],
            [[0, 1, 1], [0, 1, 1]],
        ),
        (
            [[1, 1, 1], [0, 0, 0]],
            [[1, 1, 1], [0, 0, 0]],
        ),
        (
            [[0], [0]],
            [[0], [0]],
        ),
    ]

    for i, (matrix, expected) in enumerate(test_cases, 1):
        result = solution.sort_binary_rows(matrix)
        print(f"Test case {i}: matrix={matrix}")
        print(f"Result: {result}")

        if result == expected:
            print("✓ Correct!")
        else:
            print(f"✗ Incorrect, expected {expected}")
        print()


if __name__ == "__main__":
    main()