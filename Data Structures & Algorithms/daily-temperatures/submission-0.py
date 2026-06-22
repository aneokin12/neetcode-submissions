class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]

        for i, t in enumerate(temperatures): # gets index and temp for index diff
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = i - stackI
            stack.append((t, i))
        return result
