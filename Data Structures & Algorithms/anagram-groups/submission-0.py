from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        intialize a counter object for each string in strs
        maintain a defaultdict for each object in the array of type List
        if a counter object for our current string exists, add our string to the values List
        otherwise, add our counter object as a key, then add our current string
        '''
        res = defaultdict(list)
        for s in strs:
            counts = [0 for i in range(26)]
            for c in s:
                pos = ord(c) - 97 # a-z range is 97-123
                counts[pos] += 1
            res[tuple(counts)].append(s)
        
        return list(res.values())
        