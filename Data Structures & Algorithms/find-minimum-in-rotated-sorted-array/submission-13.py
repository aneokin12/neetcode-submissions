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
        while l < r:
            mid = (l + r) // 2
            
            # If mid is greater than the rightmost element, 
            # the min must be in the right unsorted halves.
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, mid could be the minimum, or the min is to the left.
            else:
                r = mid
                
        # When l == r, we've narrowed it down to the minimum element.
        return nums[l]