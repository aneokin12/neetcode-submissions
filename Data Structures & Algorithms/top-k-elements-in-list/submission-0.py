class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if not counts.get(i):
                counts[i] = 1
            else:
                counts[i] += 1
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in counts.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
