__author__ = 'drzzh'

### use two pointers to solve,  integer counts!


import string


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s1 = ""
        integer = [str(i) for i in range(10)]
        for item in s:
            if item in string.ascii_letters:
                s1 = s1 + item.lower()
            elif item in integer:
                s1 = s1 + item
        if s1 == "":
            return True
        pointer1 = s1[0]
        pointer2 = s1[len(s1) - 1]
        for i in range(int(len(s1) / 2) + 1):#crucial  careful for the boundary
            if pointer1 == pointer2:
                pointer1 = s1[i]
                pointer2 = s1[len(s1) - 1 - i]
            else:
                return False
        else:
            return True