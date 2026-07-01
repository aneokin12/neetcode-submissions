class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        starting at i = 2
        for each element in cost:
            element = element + min(cost[i-1], cost[i-2])
            this gives you prefixes which always accrue the min path
        return the smaller of cost[len-1] and cost[len-2] at the end
        '''
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
        
        return min(cost[len(cost) - 1], cost[len(cost) - 2])
        