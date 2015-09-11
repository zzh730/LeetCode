__author__ = 'drzzh'

'''
    巨特么难的一题 要求O(log(n+m)),可以想到二分查找。
        问题可以转化成find kth smallest in two sorted array
        维护 i - 1 = i + j
            如果bj-1 < ai < bj, ai就是kth smallest， 因为ai-1,bj之前有i+j+1 = k-1个元素，而且都以排序，所以ai就是第k个
        如果不是上述情况，
            aj < bj，那么必定ai < bj - 1, 因为bj之前已经有i+j+1 = k个元素，而且bj比他们都大，所以bj及bj之后的元素不可能是解
            同时ai之前的元素小于k，也不用去找

        这样题目就转化了，当n1+n2 % 2 = 1，找K
                       当n1+n2 % 2 = 0   找(K+K+1)/2

'''


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if not nums1:
            return nums2[int(n2 / 2)] if n2 % 2 else (nums2[int(n2 / 2) - 1] + nums2[int(n2 / 2)]) / 2.0
        elif not nums2:
            return nums1[int(n1 / 2)] if n1 % 2 else (nums1[int(n1 / 2) - 1] + nums1[int(n1 / 2)]) / 2.0
        if (n1 + n2) % 2:
            return self.find(nums1, n1, nums2, n2, int((n1 + n2) / 2) + 1)
        else:
            return (self.find(nums1, n1, nums2, n2, int((n1 + n2) / 2)) + self.find(nums1, n1, nums2, n2,
                                                                                    int((n1 + n2) / 2) + 1)) / 2.0

    def find(self, nums1, m, nums2, n, k):

        i = min(int(k / 2), int(m / 2)) #防止j<0
        j = k - 1 - i

        if m > n:
            return self.find(nums2, n, nums1, m, k)#防止ij越界
        if not nums1:
            return nums2[k - 1]
        elif not nums2:
            return nums1[k - 1]

        aj_1 = -2147483648 if i <= 0 else nums1[i - 1]
        bj_1 = -2147483648 if j <= 0 else nums2[j - 1]
        aj = 2147483647 if i >= m else nums1[i]
        bj = 2147483647 if j >= n else nums2[j]

        if aj_1 <= bj <= aj:
            return bj
        elif bj_1 <= aj <= bj:
            return aj

        if aj < bj:
            return self.find(nums1[i + 1:], m - i - 1, nums2, j, k - i - 1)
        else:
            return self.find(nums1, i, nums2[j + 1:], n - j - 1, k - j - 1)
