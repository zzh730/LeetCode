__author__ = 'drzzh'

'''
    用dfs会超时, 所以直接生成序列比较好
    当k<(n-1)!, 只取序列第一个数即可,
    当k>=(n-1)!, 

'''


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        nums = [x for x in range(1, n + 1)]
        result = ""
        i = n
        while (n > 0):
            if n == 1:
                result += str(nums[0])
                break
            if k < self.fac(n - 1):
                result += str(nums[0])
                nums.remove(nums[0])
                n = n - 1
                continue
            count = self.fac(n - 1)
            index = 1 + int(k / count) if k % count != 0 else int(k / count)
            first = nums[index - 1]
            nums.remove(first)
            n = n - 1
            i -= 1
            k = k - (index - 1) * count
            result = result + str(first)

        return result

    def fac(self, n):
        count = 1
        for i in range(1, n + 1):
            count *= i
        return count


a = Solution()
print(a.getPermutation(8, 37565))
