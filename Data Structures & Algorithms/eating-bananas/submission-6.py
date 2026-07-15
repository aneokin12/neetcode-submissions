class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        notes:
        the maximum k we can have is max(piles) b/c we can always eat all bananas in one pass
        the minimum k is somewhere between 0 and max(piles)
        we can check how many hours it may take each pile to be eaten by dividing each element by k and summing them
        thus, we can binary search between 0 and max(piles) to find the optimal value

        algorithm:
        - define max piles
        - define helper function to check how many hrs it will take to eat given some k
        - binary search between 0 and k to find the minimum eating speed.
            - will need to find the largest k where calc_hrs(k) > h, then return the following elem
        '''

        # helper to check hrs given eating speed
        def calc_hrs(speed: int) -> int:
            nonlocal piles
            res = 0
            for pile in piles:
                if pile % speed == 0:
                    res += pile // speed
                else:
                    res += (pile // speed) + 1 # add one to account for remaining bananas
            return res
        
        # binary search
        left = 1
        right = max(piles)
        ans = max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2
            if calc_hrs(mid) <= h:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
            print(mid, calc_hrs(mid), left, right)

        return ans

        