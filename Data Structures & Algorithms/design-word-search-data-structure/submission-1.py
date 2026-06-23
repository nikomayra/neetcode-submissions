class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            char_idx = ord(char) - ord('a')
            if not node.children[char_idx]:
                node.children[char_idx] = TrieNode()
            node = node.children[char_idx]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children:
                        if child and dfs(child, i + 1):
                            return True
                    return False
                else:
                    char_idx = ord(char) - ord('a')
                    if not node.children[char_idx]:
                        return False
                    node = node.children[char_idx]
            return node.is_end_of_word
        
        return dfs(self.root, 0)