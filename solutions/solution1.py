from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Given an array of integers `nums` and an integer `target`, 
        return all pairs of indices where the numbers add up to `target`.
        """
        seen = {}  # number -> list of indices
        result = []
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # Agregar todos los pares posibles con el número actual
                for idx in seen[complement]:
                    result.append([idx, i])
            
            # Guardar el índice actual para este número
            elif num not in seen:
                seen[num] = []
            seen[num].append(i)
            
        return result


def main():
    """Test the solution with provided examples"""
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([8, 7, 11, 3], 14),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]
    
    for i, (nums, target) in enumerate(test_cases, 1):
        result = solution.two_sum(nums, target)
        print(f"Test case {i}: nums={nums}, target={target}")
        print(f"Result: {result}")
        
        # Verify the result
        if result and len(result) == 2:
            idx1, idx2 = result
            if nums[idx1] + nums[idx2] == target:
                print("✓ Correct!")
            else:
                print("✗ Incorrect sum")
        else:
            print("✗ Invalid result format")
        print()


if __name__ == "__main__":
    main()
