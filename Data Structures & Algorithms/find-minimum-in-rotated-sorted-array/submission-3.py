class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        start left = 0, right = len - 1
        mid = left + right / 2
        if mid > right, left = mid
        else, right = mid
        '''
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while (left <= right):
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break
            
            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            


        return res


            
        