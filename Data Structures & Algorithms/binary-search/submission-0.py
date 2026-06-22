class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = start + ((end - start) // 2)
            if nums[index] == target:
                return index
            else:
                if nums[index] > target:
                    end = index - 1
                else:
                    start = index + 1
        return -1
        