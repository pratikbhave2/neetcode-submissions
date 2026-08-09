class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Where to insert?
        if len(intervals) == 0:
            return [newInterval]

        def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
            merged = []
            for interval in intervals:
                if not merged or merged[-1][1] < interval[0]:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])
            return merged

        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[0]:
                break
        
        intervals.insert(i, newInterval)

        intervals.sort()
        return merge_intervals(intervals)

