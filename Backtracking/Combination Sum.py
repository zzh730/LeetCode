__author__ = 'drzzh'

'''
    如果用一般backtracking枚举,很容易超时, 需要进行适度修枝,
        比如每次循环从index开始,避免去找之前的值
        当sum>target时直接跳出


'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    result = []

    def combinationSum(self, candidates, target):
        self.result = []
        candidates.sort()
        self.dfs(candidates, target, [], 0)
        return self.result

    def dfs(self, candidates, target, lst, sumLst):
        if sumLst == target:
            lst.sort()
            if lst not in self.result:
                self.result.append(lst)
            return
        elif sumLst > target:
            return
        else:
            for index, item in enumerate(candidates):
                if item > target:
                    continue
                else:
                    self.dfs(candidates[index:], target, lst + [item], sumLst + item)
