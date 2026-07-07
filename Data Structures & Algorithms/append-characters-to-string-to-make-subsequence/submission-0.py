class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        approach:
        - maintain a counter to track seen characters from t
        - iterate over s, increment counter each time a char is seen
        - while counter < len(t) or s has been fully iterated, perform 2)
        - return len(t) - counter
        '''
        iter_t = 0
        iter_s = 0
        while iter_t < len(t) and iter_s < len(s):
            if s[iter_s] == t[iter_t]:
                iter_t += 1
            iter_s += 1
        
        # need iter_t + 1 b/c we are 0-indexed
        return len(t) - iter_t
        

        