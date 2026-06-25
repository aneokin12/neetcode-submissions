class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        dynamic sliding window
        use a set to maintain currently seen chars
            keep count of chars, not just if they are in set
        while r < len:
            only grow window if next char is unseen
            otherwise, increment l and r
            decrement count of moved char from l, increment count of new char from r
        return l - r + 1
        '''
        char_set = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res

