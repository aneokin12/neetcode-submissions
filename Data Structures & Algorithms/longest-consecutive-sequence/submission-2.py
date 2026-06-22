class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Approach:
        One solution is to first sort the array (O(nlogn)) then iterate
        over all elements and keep track of the longest sequence (O(n)).
        This is an O(nlogn) solution.
        '''
        if nums == []:
            return 0
        nums = sorted(nums)
        print(nums)
        curr_seq = 1
        max_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_seq += 1
                print("curr_seq: ", curr_seq)
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_len = max(max_len, curr_seq)
                print("max_len: ", max_len)
                curr_seq = 1
        return max(curr_seq, max_len)


