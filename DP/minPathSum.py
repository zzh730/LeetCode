__author__ = 'drzzh'
"""
a little problem for initialize table

trick: regular DP problem

"""


def minPathSum(grid):
    table = [[999]*6]
    for i in range(len(grid)):
        table.append(grid[i])
        table[i+1].insert(0,999)
    table[0][0] = 0
    table[1][0] = 0
    table[0][1] = 0
    print(table)
    print(grid)

    for i in range(1, len(grid)+1):
        for j in range(1, len(grid[0])+1):
            table[i][j] = min(table[i - 1][j], table[i][j - 1]) + grid[i - 1][j - 1]
    return table
grid = [
    [1,2,3,4,5],
    [7,38,4,0,1],
    [0,1,0,24,56],
    [90,2,0,1,0]
]

print(minPathSum(grid))