from typing import List


class Solution:
    def paginate(self, numbers: List[int], page_length: int, page_number: int) -> List[int]:
        """
        Return the subset of numbers for the requested page.
        """
        if page_length <= 0 or page_number <= 0:
            return []

        start = (page_number - 1) * page_length
        end = start + page_length
        return numbers[start:end]


def main():
    """Test the solution with provided examples"""
    solution = Solution()

    # Test cases: (numbers, page_length, page_number)
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 2, 1),   # expect [1, 2]
        ([10, 20, 30, 40, 50], 2, 3), # expect [50]
        ([7, 8, 9], 4, 2),            # expect []
        ([], 3, 1)                    # expect []
    ]

    for i, (numbers, page_length, page_number) in enumerate(test_cases, 1):
        result = solution.paginate(numbers, page_length, page_number)
        print(
            f"Test case {i}: numbers={numbers}, page_length={page_length}, page_number={page_number}"
        )
        print(f"Result: {result}")
        print()


if __name__ == "__main__":
    main()
