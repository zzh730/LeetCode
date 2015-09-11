#!/usr/bin/python
__author__ = 'drzzh'

"""
用一个queue储存不同的值，每次都pop最前面的值
用一个hashtable储存不同字符的index，用num来维护字符长度


"""



def lengthOfLongestSubstringTwoDistinct(s):
    dic = {}
    stack = []
    num = 0
    result = 0
    for index, item in enumerate(s):
        if item not in stack:
            stack.append(item)
        else:
            stack.remove(item)
            stack.append(item)
        dic[item] = index
        if len(stack) <= 2:
            num += 1
        elif len(stack) > 2:
            if num > result:
                result = num
            num = index - dic[stack[0]]
            del dic[stack[0]]
            del stack[0]
    if num > result:
        result = num
    return result


print(lengthOfLongestSubstringTwoDistinct("adfddddddbaccc"))