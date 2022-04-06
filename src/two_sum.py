from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums[:])
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], right]

            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
