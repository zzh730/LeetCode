__author__ = 'drzzh'

'''
容易想到的方法是：
    用一个hashtable维护key，value
    用一个list维护key的使用频率

    Time:O(n)
    Space:O(n)

'''

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.frequency = []

    # @return an integer
    def get(self, key):
        result = -1
        if key in self.dic:
            result = self.dic[key]
            self.swap(self.frequency.index(key), key)
        return result

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.get(key) > 0:
            self.dic[key] = value
            self.swap(self.frequency.index(key), key)
        else:
            if len(self.frequency) >= self.capacity:
                out = self.frequency.pop()
                del self.dic[out]
            self.frequency.insert(0, key)
            self.dic[key] = value

    def swap(self, index, key):
        del self.frequency[index]
        self.frequency.insert(0, key)