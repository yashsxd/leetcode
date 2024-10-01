class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_water = 0

        while i < j:
            max_water = max(max_water, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]: i += 1
            else: j -= 1
        return max_water