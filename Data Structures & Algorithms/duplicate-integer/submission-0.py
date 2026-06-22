class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {key:0 for key in nums}
        for num in nums:
            map[num] += 1
            if map[num] > 1:
                return True
        return False
            
         