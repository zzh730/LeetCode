__author__ = 'drzzh'


"""
正序找最小，逆序找最大

本来一道很简单的DP，脑子没绕过来弯
能很早分析出要找最大差值，仅要求最小值在最大值之前
各种直译题设条件，最后绕晕

其实就是recursion result = max（result，current result）
然后更新最小值即可.因为low一直是当前列表里的最小值

    time:O(n)
    space:O(1)

"""

def maxProfit(prices):
    if prices == []:
        return 0
    low = prices[0]
    result = 0
    for item in prices[1:]:
        result = max(result, item - low)
        low = min(low, item)
    return result


A = [100,90,1,2]
print(maxProfit(A))
