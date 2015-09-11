__author__ = 'drzzh'


'''
    思路很简单，就是radixsort每一位，然后从后往前加数就行了
    注意一点是在原始数组前sort一下，这个比如830，8308这样， 830就会在8308之前就小于8308
'''

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums.sort()
        dic = dict(zip([str(i) for i in range(10)], [[] for i in range(10)]))
        for num in nums:
            temp = str(num)
            dic[temp[0]].append(temp)
        j = 9
        result = ""
        while j > -1:
            i = str(j)
            dic[i] = self.radixsort(dic[i], i)[::-1]
            for k in dic[i]:
                result += k
            j -= 1
        return "0" if result[0] == '0' else result

    def radixsort(self, nums, first):
        length = 1
        for i in nums:
            if len(i) > length:
                length = len(i)
        i = length - 1
        while i > -1:
            temp = [[] for x in range(10)]
            for k in nums:
                num = max(k[-1], first) if i > len(k) - 1 else k[i]
                temp[int(num)].append(k)
            nums = []
            for lst in temp:
                nums.extend(lst)
            i -= 1
        return nums
