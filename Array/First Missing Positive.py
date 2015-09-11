__author__ = 'drzzh'

'''
    思路： 对于k个正数，缺失的正数会在[1,k+1]范围内，
        1. partition： 把正数放在前k个里
        2. 对于k+1个数，如果A[i](0<i<k)在A里面，就把A[A[i]]设为负，这样第一个为正的数的坐标就是要找的数

        The basic idea is for any k positive numbers (duplicates allowed),
        the first missing positive number must be within [1,k+1].
        The reason is like you put k balls into k+1 bins, there must be a bin empty,
        the empty bin can be viewed as the missing number.

        1.  Unfortunately, there are 0 and negative numbers in the array, so firstly I think of using partition technique
            (used in quick sort) to put all positive numbers together in one side. This can be finished in O(n) time, O(1) space.

        2.  After partition step, you get all the positive numbers lying within A[0,k-1].
            Now, According to the basic idea, I infer the first missing number must be within [1,k+1].
            I decide to use A[i] (0<=i<=k-1) to indicate whether the number (i+1) exists. But here I still have to
            main the original information A[i] holds. Fortunately, A[i] are all positive numbers, so I can set them to negative
            to indicate the existence of (i+1) and I can still use abs(A[i]) to get the original information A[i] holds.

        3.  After step 2, I can again scan all elements between A[0,k-1] to find the first positive element A[i],
            that means (i+1) doesn't exist, which is what I want.

    Time: O(n)
    Space: O(1)
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        nums, k = self.part(nums)
        index = -1
        for i in range(k):
            target = abs(nums[i])
            if target <= k:
                nums[target - 1] = -nums[target - 1] if nums[target - 1] > 0 else nums[target - 1]
        for i in range(k):
            if nums[i] > 0:
                index = i
                break
        return index + 1 if index != -1 else k + 1

    def part(self, nums):
        q = -1
        for index, i in enumerate(nums):
            if i > 0:
                q += 1
                if index != q:
                    temp = nums[q]
                    nums[q] = i
                    nums[index] = temp
        return nums, q + 1
