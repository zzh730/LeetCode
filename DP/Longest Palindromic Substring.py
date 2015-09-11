__author__ = 'drzzh'

'''
    回文算法的核心,避免重复计算: 从中间展开,每次查两边相不相等

    第一种算法经典DP, Time:O(n^2)
                    Space: O(N^2)
                    但是并没通过
    第二种也是dp, Space: O(1)
                对于每个元素从两边开始展开,
                注意的是分两种情况, 一个是 i,i----单个字母,
                                另一个是i,i+1-----abba这种
'''


class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        length = len(s)
        result = [[0 for j in range(length)] for i in range(length)]
        maxlen, start, end = 0, 0, 0
        for i in range(length):
            result[i][i] = 1
        for k in range(length):
            i = 0
            while i + 1 <= k < length - i - 1:
                if result[k - i][k + i] and s[k - i - 1] == s[k + i + 1]:
                    result[k - i - 1][k + i + 1] = 1
                    if 2 * (i + 1) > maxlen:
                        maxlen = 2 * (i + 1)
                        start = k - i - 1
                        end = k + i + 2
                i += 1
        return s[start:end]


class Solution2:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        length = len(s)
        result = ""
        if length == 1:
            return s
        for i in range(length - 1):
            temp = self.goAround(s, length, i, i)
            if len(temp) > len(result):
                result = temp
            temp = self.goAround(s, length, i, i + 1)
            if len(temp) > len(result):
                result = temp
        return result

    def goAround(self, s, length, i, j):
        if s[i] != s[j]:
            return ""
        k = 0
        while i - k - 1 > -1 and j + k + 1 < length:
            if s[i - k - 1] == s[j + k + 1]:
                k += 1
            else:
                break
        return s[i - k:j + k + 1]


a = Solution()
a = a.longestPalindrome(
    "vaomxdtiuwqlwhgutkhxxhccsgvyoaccuicgybnqnslogtqhblegfudagpxfvjdacsxgevvepuwthdtybgflsxjdmmfumyqgpxatvdypjmlapccaxwkuxkilqqgpihyepkilhlfkdrbsefinitdcaghqmhylnixidrygdnzmgubeybczjceiybowglkywrpkfcwpsjbkcpnvfbxnpuqzhotzspgebptnhwevbkcueyzecdrjpbpxemagnwmtwikmkpqluwmvyswvxghajknjxfazshsvjkstkezdlbnkwxawlwkqnxghjzyigkvqpapvsntojnxlmtywdrommoltpbvxwqyijpkirvndwpgufgjelqvwffpuycqfwenhzrbzbdtupyutgccdjyvhptnuhxdwbmdcbpfvxvtfryszhaakwshrjseonfvjrrdefyxefqfvadlwmedpvnozobftnnsutegrtxhwitrwdpfienhdbvvykoynrsbpmzjtotjxbvemgoxreiveakmmbbvbmfbbnyfxwrueswdlxvuelbkrdxlutyukppkzjnmfmclqpkwzyylwlzsvriwomchzzqwqglpflaepoxcnnewzstvegyaowwhgvcwjhbbstvzhhvghigoazbjiikglbqlxlccrwqvyqxpbtpoqjliziwmdkzfsrqtqdkeniulsavsfqsjwnvpprvczcujihoqeanobhlsvbzmgflhykndfydbxatskf")

print(a)
