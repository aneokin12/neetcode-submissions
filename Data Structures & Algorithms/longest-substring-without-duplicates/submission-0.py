class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        unique_chars = set()
        for r in range(len(s)):
            while s[r] in unique_chars:
                unique_chars.remove(s[l])
                l += 1
            unique_chars.add(s[r])
            res = max(res, r - l + 1)
        return res


        