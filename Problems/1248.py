from typing import List

# Time Complexity - O(n)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Array to hold the indices of the odd values
        odds_map = []
        # Variable to store the number of nice subarrays
        nice_count = 0

        # Traverse the nums list to identify the odd numbers and add their indices to odds_map
        for index, num in enumerate(nums):
            if num % 2 == 1:
                odds_map.append(index)

        for index in range(0, len(odds_map)):
            # left_pointer -> odds_map index for the first odd number of the subarray
            # right_pointer -> odds_map index for the last odd number of the subarray
            left_pointer, right_pointer = index, index + (k - 1)
            # evens_to_left -> number of even numbers to the left of the starting
            # odd number in the subarray
            # evens_to_right -> number of even numbers to the right of the ending
            # odd number in the subarray
            evens_to_left, evens_to_right = 0, 0

            # Break the loop if the right pointer is greater than or equal to the size of odds_map
            if right_pointer >= len(odds_map):
                break

            if left_pointer == 0:
                # When the left pointer is 0, evens_to_left is the index of the first odd number
                evens_to_left = odds_map[left_pointer]
            else:
                # When the left pointer is not 0, evens_to_left is the difference between
                # the current and previous odd indices minus 1
                evens_to_left = odds_map[left_pointer] - odds_map[left_pointer - 1] - 1

            if right_pointer == len(odds_map) - 1:
                # When the right pointer is the last element in odds_map, evens_to_right
                # is the number of elements left in the original array
                evens_to_right = len(nums) - odds_map[right_pointer] - 1
            else:
                # When the right pointer is not the last odd number, evens_to_right
                # is the difference between the next and current odd indices minus 1
                evens_to_right = odds_map[right_pointer + 1] - odds_map[right_pointer] - 1

            # Calculate the number of valid subarrays
            # 1 is added to both variables to include the starting and ending odd numbers
            # Example: nums = [2, 2, 1, 4, 1, 10], k = 2
            # As the k is 2, there is one valid combination of odd numbers:
            # 1 at index 2 and 1 at index 4.
            # evens_to_left = 2, evens_to_right = 1, resulting in 6 valid subarrays.
            # Valid subarrays:
            # [2, 2, 1, 4, 1], [2, 2, 1, 4, 1, 10],
            # [2, 1, 4, 1], [2, 1, 4, 1, 10],
            # [1, 4, 1], [1, 4, 1, 10]
            nice_count += (evens_to_left + 1) * (evens_to_right + 1)

        return nice_count


print(f"{Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2,1], k = 2)}\nExpected: 19")
print(f"{Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)}\nExpected: 16")
print(f"{Solution().numberOfSubarrays(nums = [1,1,2,1,1], k=3)}\nExpected: 2")
print(f"{Solution().numberOfSubarrays(nums = [2,4,6], k = 1)}\nExpected: 0")
print(f"{Solution().numberOfSubarrays(nums = [1,1,1,1,1], k = 1)}\nExpected: 5")
print(
    f"{Solution().numberOfSubarrays(nums = [45627,50891,94884,11286,35337,46414,62029,20247,72789,89158,54203,79628,25920,16832,47469,80909], k = 1)}\nExpected: 28"
)
