class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            char_idx = ord('a') - ord(char)
            if not node.children[char_idx]:
                node.children[char_idx] = TrieNode()
            node = node.children[char_idx]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            char_idx = ord('a') - ord(char)
            if not node.children[char_idx]:
                return False
            node = node.children[char_idx]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            char_idx = ord('a') - ord(char)
            if not node.children[char_idx]:
                return False
            node = node.children[char_idx]
        return True
        