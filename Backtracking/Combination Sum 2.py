__author__ = 'drzzh'

'''
    创下了oj时间最长记录T.T

'''


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    result = []

    def combinationSum2(self, candidates, target):
        self.result = []
        candidates.sort()
        self.dfs([], 0, candidates, target)
        return self.result

    def dfs(self, lst, sumLst, candidates, target):
        if sumLst == target:
            if lst not in self.result:
                self.result.append(lst)
            return
        elif sumLst > target:
            return
        else:
            for index, item in enumerate(candidates):
                if item > target:
                    break
                else:
                    self.dfs(lst + [item], sumLst + item, candidates[index + 1:], target)
