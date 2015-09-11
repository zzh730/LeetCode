__author__ = 'drzzh'
"""
brute force
tricky case:
    1) empty case, either needle or haystack
    2) needle length is greater than haystack
    3) needle locates at the end of the haystack, catch off-by-one step,  this one is tricky!!!!
    4) avoid redundent comparsion, use part of haystack not all of the haystack!!!

    Time : O(mn)
"""
def strStr( haystack, needle):
    if needle == "":
        return 0
    elif haystack == "":
        return -1
    if len(needle) > len(haystack):
        return -1
    elif len(needle) == len(haystack):
        if needle == haystack:
            return 0
        else:
            return -1
    else:
        for index1 in range(len(haystack) - len(needle) + 1):
            pointer1 = haystack[index1]
            pointer2 = needle[0]

            if pointer1 == pointer2:
                for index2 in range(1, len(needle)):
                    pointer1 = haystack[index1 + index2]
                    pointer2 = needle[index2]
                    if pointer1 != pointer2:
                        break
                else:
                    return index1
        else:
            return -1