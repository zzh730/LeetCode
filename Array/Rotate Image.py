__author__ = 'drzzh'


'''
一般的思路是先reverse，然后a[i][j] = a[j][i] for j in range(i)

'''



'''
Most Direct - 52 ms

A 100% in-place solution.
It even reads and writes each matrix element only once and doesn't even use an extra temporary variable to hold them.
It walks over the "top-left quadrant" of the matrix and directly rotates each element with the three corresponding
elements in the other three quadrants.
Note that I'm moving the four elements in parallel and that [~i] is way nicer than [n-1-i].
'''

class Solution1:
    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]

'''
List Comprehension - 60 ms

If you don't like zip, you can use a nested list comprehension instead:
'''
class Solution2:
    def rotate(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]




'''
Flip Flip - 40 ms

Basically the same as the first solution, but using reverse instead of [::-1]
and transposing the matrix with loops instead of zip. It's 100% in-place,
just instead of only moving elements around, it also moves the rows around.

'''
class Solution3:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]