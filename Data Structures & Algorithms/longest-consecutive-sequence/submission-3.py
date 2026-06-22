class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Approach:
        One solution is to first sort the array (O(nlogn)) then iterate over all elements and keep track of the longest sequence (O(n)). This is an O(nlogn) solution.
        
        Optimal solution:
        1) Convert array into hash set
        2) Iterate through array using index i
            - If set[i-1] doesn't exist, that is a sequence start
            - while set[i+1] exists, increment max_seq count
            - remove each element you encounter from the set
            - continue until no more elements in sequence, then go to next start_seq if it exists
        3) return max_seq count
        '''
        if nums == []:
            return 0
        set_nums = set(nums)
        max_seq = 1
        for n in set_nums:
            if n - 1 not in set_nums:
                curr = 1
                while n + curr in set_nums:
                    curr += 1
                    max_seq = max(curr, max_seq)
        return max_seq



