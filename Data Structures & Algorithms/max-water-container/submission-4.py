class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. set l = 0, r = len - 1
        2. area = min(h[l], h[r]) * (r - l)
        3. move left or right depending on which min is bigger
            - if min(l+1, r) > min(l, r-1), move left over 1
            - else, move right over 1
        4. repeat 3) while l < r
        5. return maximum value captured
        '''
        res = 0
        l = 0
        r = len(heights) - 1
        while (l < r):
            area = min(heights[l], heights[r]) * (r - l)
            if area > res:
                res = area
            # move l and r
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return res
        