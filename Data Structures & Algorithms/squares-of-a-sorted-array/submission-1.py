from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negatives = deque()
        # append all numbers to a second array (deque)
        while len(nums) > 0 and nums[0] < 0:
            front = nums.pop(0)
            negatives.appendleft(front)
        # now run insertion sort on two arrays
        res = []

        while len(nums) > 0 and len(negatives) > 0:
            if nums[0] ** 2 <= negatives[0] ** 2:
                res.append(nums.pop(0) ** 2)
            else:
                res.append(negatives.popleft() ** 2)
        
        remaining = nums if len(nums) > 0 else negatives

        for r in remaining:
            res.append(r ** 2)
        
        return res

                

