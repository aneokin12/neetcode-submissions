class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = float('inf')
        curr_max = 0
        for p in prices:
            curr_min = min(curr_min, p)
            curr_diff = p - curr_min
            curr_max = max(curr_diff, curr_max)
        return curr_max


        