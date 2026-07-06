class Solution:
    def compress(self, chars: List[str]) -> int:
        # if chars == 
        # pointer and counter init
        i = 0
        while i < len(chars):
            count = 1
            # increase count for consecutive elems
            while i + 1 < len(chars) and chars[i+1] == chars[i]:
                chars.pop(i+1)
                count += 1
            # when count is set, insert it into the array in rev order
            if count > 1:
                for c in str(count)[::-1]:
                    chars.insert(i+1, c)
                i = i + len(str(count)) + 1
            else:
                i = i + 1
        
        return len(chars)
