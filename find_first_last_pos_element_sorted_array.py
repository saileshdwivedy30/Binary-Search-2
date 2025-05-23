# Perform two binary searches to find the first and last positions of the target.
# First search looks for the leftmost index and second search looks for the rightmost index.
# If the target is not found, return [-1, -1].

# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        # First occurrence
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1  # look left
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if first == -1:
            return [-1, -1]  # Target not found

        # Last occurrence
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1  # look right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]