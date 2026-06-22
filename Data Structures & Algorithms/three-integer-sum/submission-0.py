class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Approach:
        1. Sort array
        2. Iterate over each element in array (i)
            - For each element, we must find two more whose sum = -1*nums[i]  
            - This can be done by placing one pointer to the right (i+1) and one pointer at the end.
            - if sum of all three is two large, move right pointer left. vice versa
        '''
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0 and [nums[i], nums[left], nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
