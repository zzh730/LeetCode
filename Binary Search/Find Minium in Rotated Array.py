__author__ = 'drzzh'

'''
看见有序直接往二分想： 数组只被rotate一次,如果数组中间数都大于最后的数
那么直接查找右边就行了，反之查左半边

Time: O(logn)


'''



class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        low = 0
        high = len(num) - 1
        while low < high:
            mid = int((low + high) / 2)
            if num[mid] > num[high]:
                low = mid + 1
            else:
                high = mid
        return num[low]