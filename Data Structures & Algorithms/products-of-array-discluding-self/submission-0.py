class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Approach:
        Create a prefix and suffix array. Prefix array stores product of all vals before that index, suffix stores product of all after
        i.e input = [1, 2, 3, 4, 5]
        prefix = [1, 1, 2, 6, 24]
        suffix = [120, 60, 20, 5, 1] = rev([1, 5, 5*4, 5*4*3, 5*4*3*2])
        
        Finally, output[i] = prefix[i] * suffix[i]
        '''
        pre = [1]
        suf = [1]
        out = []
        for i in range(1, len(nums)):
            pre.append(pre[i - 1] * nums[i - 1])
            suf.append(nums[len(nums) - i] * suf[i - 1])
        suf = suf[::-1]
        for i in range(len(nums)):
            out.append(pre[i] * suf[i])
        return out
        