__author__ = 'drzzh'
"""
uniquePath的变形问题，主要难点在于：
    1.如何对包含障碍的格点进行计算，其实就是把那点的值赋0即可
    2.如何初始化table：
        1，第一行：如果有了障碍，之后所有值为0，要不就是1
        2，第一列，如果之前有了障碍，之后所有值为0，反之为1

    time: O(MN)
    space:O(MN)
"""

def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid == []:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    table = [[0 for j in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                if j == 0:
                    if obstacleGrid[i][j] == 1:
                        table[i][j] = 0
                    else:
                        table[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        table[i][j] = 0
                    elif obstacleGrid[i][j] != 1 and table[i][j - 1] == 0:
                        table[i][j] = 0
                    else:
                        table[i][j] = 1
            else:
                if j == 0:
                    if obstacleGrid[i][j] == 1:
                        table[i][j] = 0
                    elif obstacleGrid[i][j] != 1 and table[i - 1][j] == 0:
                        table[i][j] = 0
                    else:
                        table[i][j] = 1
                else:
                    table[i][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                table[i][j] = 0
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m - 1][n - 1]

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print(uniquePathsWithObstacles(grid))


'''
一个space为o（1）的方法，边算变填表

 public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    int m = obstacleGrid.length;
    int n = obstacleGrid[0].length;

    for (int r = m - 1; r >= 0; r--) {
        for (int c = n - 1; c >= 0; c--) {
            if (obstacleGrid[r][c] == 1) obstacleGrid[r][c] = 0;
            else {
                if (r == m - 1 && c == n - 1) obstacleGrid[r][c] = 1;
                else if (r == m - 1) obstacleGrid[r][c] = obstacleGrid[r][c + 1];
                else if (c == n - 1) obstacleGrid[r][c] = obstacleGrid[r + 1][c];
                else obstacleGrid[r][c] = obstacleGrid[r][c + 1] + obstacleGrid[r + 1][c];
            }
        }
    }

    return obstacleGrid[0][0];
}

'''