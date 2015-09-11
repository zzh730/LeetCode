__author__ = 'drzzh'

'''
一道简单的dp，类似于climb stairs，tricky的地方在于对于0的判断：
    1. 当前为0，那只有10和20能行，f(n) = f(n-2)
    2. 对于11-19，21-26 可以两种方法来decode： f(n) = f(n-1) + f(n-2)
    3. 对于01-09，27-99，f(n) = f(n-1)
    4. 以0开头的一律不行
    5. 空间复杂度可以从O(n)优化到O(1)，仅用first，second来维护窗口


    Time: O(n)
    Space: O(1)
'''



class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        first = 1
        second = 1
        for i in range(1, len(s)):
            if s[i] == '0':                     # only 10 and 20 are ok
                if s[i - 1] in ['1', '2']:
                    result = first
                else:
                    return 0
            elif 9 < int(s[i - 1:i + 1]) < 27:  # case 11-19 21-26
                result = first + second
            else:                               # case 01-09 27-99
                result = second
            first = second
            second = result
        return result


a = Solution()
print(a.numDecodings("7206"))
