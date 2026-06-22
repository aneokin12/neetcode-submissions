class Solution:
    def isValid(self, s: str) -> bool:
        ops = {'}': '{', ']': '[', ')': '('}
        stk = []
        for c in s:
            if c in ops.values():
                stk.append(c)
            else:
                if stk and ops[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
        return True if not stk else False
        