class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        a. count maximum frequency in a window
        b. window size - largest freq ≤ k, k fills in replacements.
        algo:
        1. iterate over s with right pointer
        2. increment count for current char and store in dict
        3. update the maxf counter using count of current char
        4. adjust the left pointer by moving it right until b. is satisfied
        5. update result by taking max of it and window size
        '''
        counter = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(maxf, counter[s[r]])

            while (r - l + 1) - maxf > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
