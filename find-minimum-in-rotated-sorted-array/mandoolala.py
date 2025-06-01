from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[0] < nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[0]
