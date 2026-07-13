import random
class Solution:



    def encode(self, strs: List[str]) -> str:
        shift = random.randint(1, 256)
        res = str(shift) + "_"
        # shift each string using ascii conversion
        for word in strs:
            for c in word:
                 res += str(chr(ord(c) + shift))
            res += chr(127)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        shift_end = s.find('_')
        shift = int(s[0:shift_end])
        # define current word start pointer
        curr_start = shift_end + 1
        while curr_start < len(s):
            curr_end = s.find(chr(127), curr_start)
            curr_word = s[curr_start:curr_end]
            curr_shifted_word = ""
            for c in curr_word:
                curr_shifted_word += chr((ord(c) - shift))
            res.append(curr_shifted_word)
            curr_start = curr_end + 1
        
        return res

