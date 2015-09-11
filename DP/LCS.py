__author__ = 'drzzh'



def LCS(a, b):
    table = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] != b[j-1]:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
            else:
                table[i][j] = table[i - 1][j - 1] + 1
    return table[len(a)][len(b)]


print(LCS("abefcd","efd"))