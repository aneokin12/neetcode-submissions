class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        fixed size sliding window
        1. choose window length of len(s1)
        2. iterate over s2 while right pointer < len
        3. if sorted(window substring) == sorted(s1), return true
        4. if not 3, return false
        '''
        for r in range(len(s1) - 1, len(s2)):
            l = r - len(s1) + 1
            window = s2[l:r+1]
            if sorted(window) == sorted(s1):
                return True
        return False

        