__author__ = 'drzzh'


"""
edge case及其多的一道题，如果单纯用if else就等着挂吧

trick：
    容易出错的地方在于lower和upper两个边界，那我们只需要将lower = lower -1, upper = upper + 1
    转换后，lower和upper就喝一般情况一样了
"""
def findMissingRanges(A, lower, upper):
        result = []
        low = lower - 1
        up = upper + 1
        if A == []:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(str(lower)+"->"+str(upper))]
        for item in A:
            if item - low in [0,1]:
                None
            elif item - low == 2:
                result.append(str(low+1))
            else:
                result.append(str(str(low+1)+"->"+str(item-1)))
            low = item
        else:
            if up - low in [0,1]:
                None
            elif up - low == 2:
                result.append(str(low+1))
            else:
                result.append(str(str(low+1)+"->"+str(up-1)))
        return result

print(findMissingRanges([], 0, 9))