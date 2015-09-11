__author__ = 'drzzh'

'''
    特殊情况注意下：
        1. 本身没有'.'，这时候加个判断即可
        2. 交换了以后返回的值要乘-1
'''


class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        sign = 1
        v1 = version1.split('.') if "." in version1 else [version1]
        v2 = version2.split('.') if "." in version2 else [version2]
        if len(v1) > len(v2):
            temp = v1
            v1 = v2
            v2 = temp
            sign = -1
        v1 += ['0'] * (len(v2) - len(v1))
        for i in range(len(v2)):
            if int(v1[i]) > int(v2[i]):
                return 1 * sign
            elif int(v1[i]) < int(v2[i]):
                return -1 * sign
        else:
            return 0


a = Solution()
