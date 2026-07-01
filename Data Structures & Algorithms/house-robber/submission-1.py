class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp problem
        can either rob house, move to skip
            - total accrued would be dp[i - 2] + nums[i]
        or skip this house, rob next one
            - total would be dp[i - 1]

        whichever total is larger, we pick that and set that index to the value
        '''
        if len(nums) == 1:
            return nums[0]
        dp = []
        # initialize first 2 indices since we are looking back by 2
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        
        return dp[len(nums) - 1]
        