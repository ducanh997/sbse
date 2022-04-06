from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result = -1

        while start <= end:
            water = min(height[start], height[end]) * (end - start)
            result = max(water, result)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return result
