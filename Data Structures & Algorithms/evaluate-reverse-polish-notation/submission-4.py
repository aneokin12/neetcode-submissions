class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Approach:
        1. Loop through tokens, parsing ops and nums differently.
            - If you encounter a num, push it onto the stack.
            - If you encounter an op, pop top two nums and push result onto the stack
        2. By the end of tokens, stack will have one num. Return it
        '''
        stk = []
        ops = ["*", "/", "+", "-"]
        for t in tokens:
            if t not in ops:
                stk.append(int(t))
            else:
                b = stk.pop()
                a = stk.pop()

                if t == "*":
                    stk.append(a * b)
                elif t == "/":
                    stk.append(int(a / b))
                elif t == "+":
                    stk.append(a + b)
                elif t == "-":
                    stk.append(a - b)
        return stk.pop()


        
        