__author__ = 'drzzh'

'''
    set('abc') ---> {'a','b','c'}
    set(['abc'])--> {'abc'}

'''
import re


class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.dic = {}

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        n = len(word)
        if n not in self.dic:
            self.dic[n] = set([word])
        else:
            self.dic[n].add(word)

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        n = len(word)
        pattern = re.compile(word)
        if n not in self.dic:
            return False
        for item in self.dic[n]:
            match = pattern.match(item)
            if match:
                return True
        return False
