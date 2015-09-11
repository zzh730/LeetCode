__author__ = 'drzzh'


class TwoSum:

    def __init__(self):
        self.dic = {}

    # @return nothing
    def add(self, number):
        if number not in self.dic:
            self.dic[number] = 1
        else:
            self.dic[number] += 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for item in self.dic:
            if (value-item) in self.dic and item in self.dic and  (value-item)!= item:
                return True
            elif (value-item == item) and self.dic[item]>1:
                return True

        else:
            return False