# Use binary search to find the minimum element in a rotated sorted array.
# Compare mid and high to decide which half to search next.
# The loop ends when low points to the smallest element.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]