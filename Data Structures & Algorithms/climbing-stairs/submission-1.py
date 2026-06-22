class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 4: 
        1 + 1 + 1 + 1
        1 + 1 + 2
        1 + 2 + 1
        2 + 1 + 1
        2 + 2
        
        n = 5
        1 + 1 + 1 + 1 + 1
        1 + 1 + 1 + 2
        1 + 1 + 2 + 1
        1 + 2 + 1 + 1
        2 + 1 + 1 + 1
        2 + 2 + 1
        2 + 1 + 2
        1 + 2 + 2

        stairs(n) = stairs(n-1) + stairs(n-2)
        '''
        stairs = [1, 2]
        for i in range(2, n):
            stairs.append(stairs[i-1] + stairs[i-2])
        return stairs[n-1]