"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        prev_end = -1
        for i in range(len(intervals)):
            cur_begining, cur_end = intervals[i].start, intervals[i].end
            if prev_end > cur_begining:
                return False
            prev_end = cur_end
            
        return True