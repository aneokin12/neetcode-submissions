class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # outer matrix bin search
        o_l, o_r = 0, len(matrix) - 1
        while o_l <= o_r:
            o_index = o_l + ((o_r - o_l) // 2)
            if matrix[o_index][0] > target:
                o_r = o_index - 1
            elif matrix[o_index][-1] < target:
                o_l = o_index + 1
            else:
                break
        # inner matrix bin search
        l, r = 0, len(matrix[o_index]) - 1
        while l <= r:
            index = l + ((r - l) // 2)
            if matrix[o_index][index] > target:
                r = index - 1
            elif matrix[o_index][index] < target:
                l = index + 1
            else: 
                return True
        return False
        