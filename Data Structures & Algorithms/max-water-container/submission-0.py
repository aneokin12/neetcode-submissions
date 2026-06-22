class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Approach:
        1. Start with left and right pointers (0 and len - 1)
        2. Calculate min(height[left], height[right]) * (right - left)
        3. store result from 2) in curr_max
        4. move the smaller bar left or right
        5. repeat while left < right
        '''
        left = 0
        right = len(heights) - 1
        curr_max = 0
        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)
            curr_max = max(curr_max, curr_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return curr_max