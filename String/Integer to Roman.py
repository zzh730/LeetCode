__author__ = 'drzzh'


dic = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M', '2000': 'MM', '3000': 'MMM'}


class Solution:
    # @param {integer} num  I X V
    # @return {string}
    def intToRoman(self, num):
        number = str(num)
        length = len(number)
        if number in dic:
            return dic[number]
        result = ""
        for i in range(length):
            digit = number[i]
            if length - i == 4:
                temp = str(int(digit) * 1000)
                result += dic[temp]
            elif length - i == 3:
                result += self.trans(digit, 'C', 'D', 'M')
            elif length - i == 2:
                result += self.trans(digit, 'X', 'L', 'C')
            elif length - i == 1:
                result += self.trans(digit, 'I', 'V', 'X')
            else:
                print("Wrong")
        return result

    def trans(self, digit, start, mid, end):
        num = int(digit)
        if 1 <= num < 4:
            return start * num
        elif num == 4:
            return start + mid
        elif num == 5:
            return mid
        elif 5 < num < 9:
            return mid + start * (num - 5)
        elif num == 9:
            return start + end
        elif num == 0:
            return ""
        else:
            print("wrong digit!")


a = Solution()
print(a.intToRoman(2000))

