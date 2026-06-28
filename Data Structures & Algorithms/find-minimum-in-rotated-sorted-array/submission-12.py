class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        need binary search
        if nums[left] < nums[mid]: array still in order -- left = mid + 1
        if nums[left] > nums[mid]: min somewhere in between -- right = mid - 1
        mid = (left + right) // 2
        '''
        l, r = 0, len(nums) - 1
        res = nums[0]

        while (l <= r):
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
    
            

        return res