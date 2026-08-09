"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_rooms = 0

        # create separae start and end lists
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        s = e = 0
        res = count = 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res