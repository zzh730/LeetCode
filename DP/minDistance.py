__author__ = 'drzzh'


"""
 是编辑距离的简化版，所有cost一样，
    1.初始化table，第一行是只进行insert的cost，第一列是只进行delete的cost，table[0][0] = 0
    2.相等的情况是走对角线


    time:O(nm)
    space:O(nm)



改进方法：time:O(n^2)
         space:      O(n)!!!
         table[i][j]只与table[i-1][j],table[i-1][j](上一行的数据)还有table[i][j-1]有关
         所以计算当前行的数据就只存前一行的数据，还有前一个更新的数据即可
         prev = delete, table[j] = replace, table[j+1] = insert


"""

def minDistance(word1, word2):
    n = len(word2)
    m = len(word1)
    if n == 0:
        return m
    if m == 0:
        return n
    if word1 == word2:
        return 0
    table = [[i for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = i
    table[0][0] = 0

    for i in range(n):
        for j in range(m):
            if word1[j] != word2[i]:
                table[i + 1][j + 1] = min(table[i][j] + 1, table[i][j + 1] + 1, table[i + 1][j] + 1)
            else:
                table[i + 1][j + 1] = table[i][j]

    return table


word1 = "ab"
word2 = "abbbb"
print(minDistance(word1, word2))


def better(word1, word2):
    n = len(word2)
    m = len(word1)
    if n == 0:
        return m
    if m == 0:
        return n
    if word1 == word2:
        return 0
    table = [j for j in range(m + 1)]

    for i in range(n):
        prev = i+1
        for j in range(m):
            if word1[j] == word2[i]:
                cur = table[j]
            else:
                cur = min(table[j], table[j+1], prev)+1
            table[j] = prev
            prev = cur
        table[m] = prev
    return table[m]