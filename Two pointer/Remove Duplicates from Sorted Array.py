__author__ = 'drzzh'


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        if len(A) == 1:
            return 1
        end = 0
        for i in range(1,len(A)):
            if A[i] != A[end]:
                end += 1
                if i != end:
                    A[end] = A[i]
        return end + 1

a = Solution()
print (a.removeDuplicates([1,1,2]))