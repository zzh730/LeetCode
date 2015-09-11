__author__ = 'drzzh'
'''
a simple DP problem,
just initialize the table and store each step
'''

def uniquePaths(m, n):
    if m == n == 0:
        return 0
    table = [[1 for index in range(n)]]
    for i in range(1,m):
        table.append([1 if index == 0 else 0 for index in range(n)])

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m - 1][n - 1]

print(uniquePaths(2,3))