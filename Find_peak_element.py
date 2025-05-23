# Use binary search to find a peak element in the array.
# If mid > mid+1, move left since a peak must exist there.
# Else move right. Eventually, low will point to a peak.

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return low
