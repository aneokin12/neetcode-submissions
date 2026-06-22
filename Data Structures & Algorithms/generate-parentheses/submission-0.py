class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            # if open = closed = n, valid
            if openN == closedN == n:
                res.append("".join(stack))
                return
            # add '(' if openN < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            # add ')' if closedN < openN
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res