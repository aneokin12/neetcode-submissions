class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        approach:
        - sort input intervals array (O(nlogn))
        - for each interval (range 1 to len), maintain curr_overlap tuple
        - if intervals[i][0] < intervals[i-1][1]:
            - curr_overlap[1] = intervals[i][1]
        - otherwise, append curr overlap, curr_overlap = intervals[i]
        '''
        # edge case: intervals length is 1
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals) # O(nlogn)
        res = []
        curr_overlap = intervals[0] 
        for i in range(1, len(intervals)):
            # check if overlap exists
            if intervals[i][0] <= curr_overlap[1]:
                curr_overlap[0] = min(curr_overlap[0], intervals[i][0])
                curr_overlap[1] = max(curr_overlap[1], intervals[i][1])
            else:
                res.append(curr_overlap)
                curr_overlap = intervals[i]
        # have to append last overlap
        res.append(curr_overlap)

        return res