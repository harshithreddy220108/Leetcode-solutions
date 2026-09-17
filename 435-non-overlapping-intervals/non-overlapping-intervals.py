class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        r=0
        l=intervals[0][1]
        for i in range(1,len(intervals)):
            cs=intervals[i][0]
            ce=intervals[i][1]
            if cs<l:
                r+=1
            else:
                l=ce
        return r