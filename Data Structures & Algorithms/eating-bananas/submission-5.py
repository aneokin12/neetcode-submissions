class Solution: 
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(speed) -> bool:
            # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower        
            return sum(math.ceil(pile / speed) for pile in piles) <= H  # faster

        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res