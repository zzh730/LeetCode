__author__ = 'drzzh'

'''
    方法是对start排序，然后分4种情况讨论：
        1. next.start in [cur.start,cur.end]
            1.next.end <= cur.end next就没用了，标记为none
            2.else 把next.end设为新的end，注意next也没用了，设为none
        2. else， 俩区间不重合，cur = next就行了



'''


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def makeinterval(intervals):
    return list(map(lambda x: Interval(x[0], x[1]), intervals))


class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        new = [(i.start, index) for index, i in enumerate(intervals)]
        new.sort()
        if not intervals:
            return []
        cur = intervals[new[0][1]]
        for i in range(1, len(intervals)):
            if cur.start <= intervals[new[i][1]].start <= cur.end:
                if intervals[new[i][1]].end <= cur.end:
                    intervals[new[i][1]] = None
                else:
                    cur.end = intervals[new[i][1]].end
                    intervals[new[i][1]] = None
            else:
                cur = intervals[new[i][1]]
        for index, i in enumerate(intervals):
            if not i:
                del intervals[index]
        return [i for i in intervals if i]
