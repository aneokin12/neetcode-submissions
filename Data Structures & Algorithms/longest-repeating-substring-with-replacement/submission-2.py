class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. Iterate through the string, counting the longest substring
        2. Keep track of the current char
        3. when you encounter a char that is not curr:
            - subtract from k and act as though it is one and continue
        4. if k = 0 and char != curr, move starting pointer to next char
        5. repeat 1-4, return max length calculated
        '''
        res = 0
        for char_code in range(ord('A'), ord('Z') + 1):
            target = chr(char_code)
            l = 0
            temp = k
            for r in range(len(s)):
                if s[r] != target:
                    temp -= 1
                while temp < 0:
                    if s[l] != target:
                        temp += 1
                    l += 1
                res = max(res, r - l + 1)
        return res