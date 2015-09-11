__author__ = 'drzzh'

'''
先把数组排序，这样可以避免一些重复情况，然后对每一个item求two sum
    two sum 可以用two pointer，两边夹逼，注意跳过重复的元素


Time: O(nlong+n^2)
Space: O(1)
'''


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        num.sort()
        if len(num) < 3:
            return []
        for index, item in enumerate(num[:len(num) - 2]):  # 扫到倒数第三个就能停了
            if index > 0 and item == num[index - 1]:  # 避免扫描是出现重复
                continue
            target = - item
            left = index + 1
            right = len(num) - 1
            while left < right:
                if num[left] + num[right] == target:
                    new = [item, num[left], num[right]]
                    result.append(new)
                    left += 1
                    right -= 1
                    while num[left] == num[left - 1] and left < right:  #
                        left += 1
                    while num[right] == num[right + 1] and left < right:  #
                        right -= 1
                elif num[left] + num[right] > target:
                    right -= 1
                else:
                    left += 1
        return result


'''
    一样的思路，就是直接调用twosum，
    注意：
        twosum得返回全部解法

'''


class Solution2:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        for index, i in enumerate(num):
            lst = self.twoSum(num[index + 1:], 0 - i)
            if lst:
                for solution in lst:
                    temp = list(solution) + [i]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
        return result

    def twoSum(self, num, target):
        p1 = 0
        p2 = len(num) - 1
        result = []
        while p1 < p2:
            if num[p1] + num[p2] == target:
                result.append((num[p1], num[p2]))
                p1 += 1
            elif num[p1] + num[p2] > target:
                p2 -= 1
            else:
                p1 += 1
        return result
