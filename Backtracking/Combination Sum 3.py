__author__ = 'drzzh'

'''
    解法详见combination sum 1


'''


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    result = []

    def combinationSum3(self, k, n):
        self.result = []
        candidates = range(1, 10)
        self.dfs(k, n, [], 0, candidates)
        return self.result

    def dfs(self, k, n, lst, sumlst, candidates):
        if len(lst) == k and sumlst == n:
            lst.sort()
            self.result.append(lst)
            return
        elif len(lst) > k or sumlst > n:
            return
        else:
            for index, item in enumerate(candidates):
                if item > n:
                    break
                else:
                    self.dfs(k, n, lst + [item], sumlst + item, candidates[index + 1:])
