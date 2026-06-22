class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Approach:
        1. Create map of brackets (keys = close, vals = corresponding open)
        2. when an open bracket is encountered, push it onto the stack
        3. when a close bracket is encountered, check the top of the stack.
            - if it corresponds, pop the top and continue.
            - if not, return false
        4. by the end of the string, the s array should be empty. 
            - if it is, return true
            - if not, return false
        '''

        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        if not s:
            return False
        stk = []
        for c in s:
            if c in brackets.values(): 
                stk.append(c)
            elif c in brackets.keys():
                if not stk or brackets[c] != stk[-1]:
                    return False
                else:
                    stk.pop()
        if stk:
            return False
        return True


