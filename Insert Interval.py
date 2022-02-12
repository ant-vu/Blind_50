class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []        
        s, e = newInterval
        for i in range(len(intervals)):
            if (intervals[i][0] <= s <= intervals[i][1]) or (intervals[i][0] <= e <= intervals[i][1]) or (s <= intervals[i][0] and e >= intervals[i][1]):
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
            else:
                res.append(intervals[i])
        res.append([s,e])
        return sorted(res)
