class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        goal: binary search target between left and right where left < target < right (trivial)
        we want to search for the target between the pivot and mid where possible
        while left <= right
            if mid < right, it's after the pivot or is the pivot.
                - if target between mid and right, search in the right half
                    - left = mid + 1
                - otherwise, search in the left half
                    - right = mid - 1
            else if mid > right, it's before the pivot or is the pivot
                - if target between left and mid, seaxch in the left half
                    - right = mid - 1
                - otherwise, search in the right half
                    - left = mid + 1
            set mid = left + (right - left) // 2
        
        return mid
        '''
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # left half sorted
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right half sorted
            else:
                # already checked for nums[mid], and target could be nums[right]
                if nums[mid] < target <= nums[right] :
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
