__author__ = 'drzzh'

'''
    '010','000'不能算作解法

'''


class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        self.res = []
        self.dfs(s, [], 1)
        return self.res

    def dfs(self, s, cur, num):
        if not s and num == 5:
            for item in cur:
                if item[0] == '0' and len(item) > 1:
                    return
            lst = '.'.join(cur)
            if lst not in self.res:
                self.res.append(lst)
            return
        elif s and (num > 5 or num == 5 and int(s) > 255):
            return
        elif not s and num < 4:
            return
        else:
            for i in range(1, 4):
                if i <= len(s) and int(s[:i]) < 256:
                    self.dfs(s[i:], cur + [s[:i]], num + 1)
