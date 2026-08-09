class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class WordDictionary:

    def __init__(self):
        self.word_dict = Trie()

    def addWord(self, word: str) -> None:
        self.word_dict.insert(word)
        
    def search(self, word: str) -> bool:

        def dfs(index: int, node: TrieNode):
            if index == len(word):
                return node.is_word

            curr_char = word[index]
            if curr_char == ".":
                for child in node.children:
                    if (dfs(index + 1, node.children[child])):
                        return True
                return False
            
            else:
                if curr_char not in node.children:
                    return False
                return dfs(index + 1, node.children[curr_char])
        return dfs(0, self.word_dict.root)
                

