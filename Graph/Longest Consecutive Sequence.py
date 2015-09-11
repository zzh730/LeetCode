__author__ = 'drzzh'

'''
naive 方法：先排序，然后去掉重复元素，最后遍历列表，记录最长的序列长度，注意最后在比较一次
    TIME: O(nlogn)
    Space: O(1)
'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        num = self.removeDeplicate(num)
        result = 0
        prev = num[0]
        if not num:
            return 0
        if len(num) == 1:
            return 1
        cur = 1
        for item in num[1:]:
            if item - prev == 1:
                cur += 1
            else:
                result = max(result, cur)
                cur = 1
            prev = item
        result = max(result, cur)
        return result

    def removeDeplicate(self, num):
        prev = num[0]
        for item in num[1:]:
            if prev == item:
                num.remove(item)
            prev = item
        return num


num = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
a = Solution()
print(a.longestConsecutive(num))



# ---------------------------------------------
'''
更加聪明的解法：把每个数字看成node，相差1就是相邻节点，选一个节点向左右遍历，断了就和之前结果比较，更新
    注意：1. 实现的时候用set，不含重复元素
         2. 用hashmap记录访问过的节点


Time:O(n)
Space:O(n)
'''


class Solution2:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if not num:
            return 0
        if len(num) == 1:
            return 1
        dic = set(num)
        result = 1
        visit = {}
        for item in dic:
            if item in visit:
                continue
            visit[item] = True
            length = 1
            cur = item
            while cur + 1 in dic:
                cur = cur + 1
                visit[cur] = True
                length += 1
            cur = item
            while cur - 1 in dic:
                cur = cur - 1
                visit[cur] = True
                length += 1
            result = max(result, length)
        return result