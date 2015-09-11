__author__ = 'drzzh'


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        p1, p2 = len(height) - 1, 0
        area = 0

        if not height or len(height) == 1:
            return 0
        while p1 > p2:
            area = max(area, (p1 - p2) * min(height[p1], height[p2]))
            if height[p1] > height[p2]:
                p2 += 1
            else:
                p1 -= 1
        return area


a = Solution()
print(a.maxArea(
    [17, 84, 58, 48, 40, 91, 54, 35, 97, 17, 40, 59, 57, 61, 23, 15, 68, 93, 72, 2, 34, 66, 36, 26, 25, 2, 83, 20, 27,
     41, 44, 96, 25, 2, 45, 17, 45, 51, 52, 42, 68, 92, 54, 77, 5, 29, 93, 73, 23, 17, 75, 57, 83, 12, 36, 60, 66, 71,
     33, 45, 12, 77, 41, 89, 80, 38, 6, 25, 41, 10, 20, 61, 2, 74, 39, 7, 3, 32, 33, 78, 1, 60, 88, 84, 24, 24, 96, 42,
     95, 29, 39, 59, 7, 81, 48, 39, 71, 6, 16, 13, 16, 36, 26, 70, 62, 65, 29, 18, 49, 14, 96, 50, 75, 84, 86, 51, 60,
     83, 94, 55, 64, 33, 14, 23, 66, 14, 62, 90, 72, 31, 55, 88, 19, 81, 10, 82, 47, 40, 0, 48, 54, 48, 99, 81, 33, 85,
     33, 93, 20, 27, 1, 85, 12, 67, 8, 79, 82, 23, 21, 6, 54, 76, 95, 73, 57, 5, 7, 56, 97, 7, 5, 52, 56, 4, 85, 41, 41,
     18, 86, 14, 97, 87, 99, 10, 55, 59, 41, 89, 82, 62, 95, 88, 38, 42, 14, 47, 0, 21, 4, 97, 81, 9, 1, 89, 65, 87, 82,
     6, 5, 68, 20, 55, 56, 71, 65, 63, 31, 58, 4, 65, 72, 51, 6, 62, 94, 72, 9, 94, 45, 13, 91, 26, 74, 45, 67, 39, 32,
     1, 98, 89, 70, 70, 44, 78, 42, 61, 93, 25, 71, 97, 42, 43, 48, 48, 5, 94, 72, 67, 88, 18, 32, 32, 96, 7, 77, 64,
     98, 61, 65, 48, 2, 87, 19, 47, 17, 13, 60, 10, 38, 32, 7, 32, 27, 8, 81, 33, 2, 5, 52, 43, 23, 84, 27, 20, 43, 56,
     36, 94, 17, 53, 42, 19, 41, 61, 18, 58, 74, 79, 21, 64, 63, 80, 97, 90, 88, 30, 75, 43, 35, 27, 86, 59, 64, 65, 31,
     59, 21, 67, 53, 38, 20, 96, 9, 61, 9, 80, 72, 36, 11, 93, 52, 74, 73, 49, 16, 14, 31, 92, 57, 67, 71, 95, 78, 87,
     60, 9, 47, 33, 76, 52, 23, 48, 0, 32, 62, 62, 64, 34, 98, 75, 79, 50, 1, 4, 52, 18, 18, 83, 62, 27, 2, 85, 22, 32,
     25, 34, 93, 24, 67, 21, 76, 90, 70, 29, 75, 32, 91, 39, 18, 41, 67, 97, 43, 68, 1, 95, 38, 20, 31, 0, 99, 85, 38,
     74, 70, 63, 8, 63, 39, 28, 85, 15, 70, 7, 96, 97, 39, 87, 37, 9, 80, 56, 6, 24, 24, 7, 71, 15, 79, 2, 67, 79, 40,
     5, 53, 10, 20, 13, 73, 59, 93, 10, 27, 64, 17, 23, 13, 8, 63, 2, 17, 43, 58, 75, 67, 35, 35, 91, 50, 66, 93, 17,
     97, 85, 75, 2, 95, 95, 16, 21, 7, 61, 31, 34, 77, 1, 9, 91, 61, 72, 93, 31, 16, 52, 6, 35, 87, 93, 26, 37, 60, 72,
     6, 57, 57, 81, 60, 5, 77, 28, 26, 36, 89, 57, 70, 67, 10, 79, 58, 72, 4, 3, 3, 72, 55, 61, 7, 94, 55, 86, 83, 15,
     10, 90, 24, 19, 71, 84, 24, 0, 12, 50, 36, 54, 60, 58, 73, 70, 90, 83, 94, 94, 86, 97, 66, 94, 11, 25, 88, 66, 63,
     72, 81, 73, 62, 5, 45, 85, 42, 69, 38, 6, 20, 26, 60, 32, 85, 85, 2, 27, 68, 97, 73, 7, 46, 91, 1, 57, 68, 89, 23,
     32, 61, 56, 57, 75, 14, 2, 13, 8, 24, 51, 14, 44, 77, 27, 76, 14, 12, 30, 93, 33, 79, 66, 40, 26, 9, 41, 83, 78,
     82, 59, 62, 96, 67, 71, 71, 33, 26, 36, 41, 50, 87, 56, 46, 17, 35, 74, 83, 99, 4, 77, 84, 84, 95, 24, 62, 5, 17,
     45, 35, 0, 56, 97, 96, 24, 20, 19, 57, 46, 56, 51, 96, 95, 59, 94, 12, 94, 68, 48, 45, 73, 77, 30, 9, 72, 54, 71,
     29, 24, 68, 16, 24, 77, 65, 72, 53, 86, 43, 10, 32, 99, 13, 81, 47, 72, 75, 11, 66, 44, 59, 12, 69, 36, 42, 30, 61,
     48, 53, 90, 24, 73, 59, 0, 50, 24, 72, 3, 10, 68, 66, 43, 19, 79, 76, 66, 52, 51, 78, 70, 47, 89, 34, 68, 26, 28,
     98, 39, 77, 3, 29, 53, 77, 40, 54, 79, 65, 26, 35, 75, 46, 53, 70, 66, 32, 46, 32, 36, 50, 62, 59, 49, 52, 93, 18,
     30, 74, 68, 69, 3, 72, 50, 56, 1, 91, 10, 80, 56, 89, 67, 31, 35, 20, 54, 1, 5, 52, 34, 41, 2, 48, 52, 52, 0, 98,
     22, 30, 72, 42, 51, 75, 14, 2, 31, 67, 93, 94, 0, 1, 83, 67, 32, 18, 88, 38, 20, 93, 91, 6, 86, 93, 54, 39, 97, 7,
     89, 71, 89, 61, 14, 41, 88, 80, 43, 71, 0, 88, 65, 0, 89, 48, 67, 73, 67, 55, 12, 39, 48, 3, 45, 87, 48, 51, 26,
     98, 58, 15, 21, 48, 28, 35, 89, 16, 68, 84, 87, 68, 24, 5, 68, 13, 53, 87, 38, 20, 43, 2, 11, 43, 57, 56, 30, 58,
     8, 8, 56, 18, 75, 29, 66, 55, 65, 7, 71, 85, 43, 11, 5, 67, 16, 73, 32, 21, 12, 23, 42, 7, 25, 5, 3, 35, 62, 85,
     93, 22, 94, 1, 40, 21, 30, 59, 77, 47, 18, 0, 32, 62, 63, 37, 81, 79, 62, 66, 1, 27, 89, 95, 34, 66, 0, 37, 1, 14,
     23, 94, 88, 69, 95, 29, 90, 26, 40, 67, 25, 58, 20, 58, 72, 83, 47, 6, 15, 62, 72, 16, 89, 13, 63, 23, 79, 15, 61,
     33, 30, 36, 27, 18, 5, 75, 99, 95, 53, 91, 15, 78, 50, 35, 88, 74, 70, 36, 32, 85, 50, 4, 1, 39, 69, 16, 14]))
