class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Approach:
        We need a set of some sort. One set for each row, column, and sub-box.
        We can iterate through each element of the board in O(n^2) time and assign
        it to the appropriate row, column, and sub-box set. If we ever encounter an element
        that already exists in some subset, return true. else, return false.
        Logic:
            - Use two nested for loops, r for row, c for col
            - integer divide r and c by 3 to get the right ixi sub-box
            - ex: board[8][8] goes into sub-box (2,2)
        '''
        # Initialization
        n = len(board)
        rows = [set() for i in range(n)]
        cols = [set() for i in range(n)]
        subs = {}
        for i in range(3):
            for j in range(3):
                key = (i, j)
                subs[key] = set()
        # Main loop
        for r in range(n):
            for c in range(n):
                spot = board[r][c]
                if spot != ".":
                    if spot not in rows[r] and spot not in cols[c] and spot not in subs[(r//3, c//3)]:
                        rows[r].add(spot)
                        cols[c].add(spot)
                        subs[(r//3, c//3)].add(spot)
                    else:
                        return False
        return True

