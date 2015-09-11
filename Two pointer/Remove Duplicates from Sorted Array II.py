__author__ = 'drzzh'


'''
Two pointer的应用， i扫数组，end是新数组最后的元素，
    这题要保留多一个重复元素，所以只需要比较end-1和i，因为有序数组的性质

'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 3:
            return len(A)
        end = 1
        for i in range(2, len(A)):
            if A[i] != A[end - 1]:
                end += 1
                A[end] = A[i]
        return end + 1