class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i # need two counters in case '#' is in string
            while s[j] != '#':
                print("j:"+str(j))
                j += 1
            length = int(s[i:j])
            print("--")
            i = j + 1
            print("i:"+str(i))
            print("--")
            j = i + length
            print("j:"+str(j))
            res.append(s[i:j])
            i = j
        return res
