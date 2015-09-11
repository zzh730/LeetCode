'''
    最后单词结尾要加上结束符, 要不"abc","ab"不能区分
'''


class TrieNode:
    # Initialize your data structure here.
    def __init__(self, val=None):
        self.next = []
        self.val = val
        self.stop = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.count = 0

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        self.count += 1
        for char in word:
            for child in cur.next:
                if child.val == char:
                    cur = child
                    break
            else:
                new = TrieNode(char)
                cur.next.append(new)
                cur = new
        cur.stop = self.count

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        cur = self.root
        for char in word:
            for child in cur.next:
                if child.val == char:
                    cur = child
                    break
            else:
                return False
        return True if cur.stop else False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        cur = self.root
        for char in prefix:
            for child in cur.next:
                if child.val == char:
                    cur = child
                    break
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")


a = Trie()
a.insert("abc")
a.insert("april")
a.insert("banana")
a.insert("abron")

print(a.search("f"))
print(a.search("abc"))
print(a.search("abron"))
