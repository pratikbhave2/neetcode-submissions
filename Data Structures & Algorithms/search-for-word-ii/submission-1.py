class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()

        for word in words:
            self.trie.insert(word)

        # DFS + Backtracking
        found = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, node, path):
            if node.is_word:
                found.add(path)
                node.is_word = False
            
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and board[nr][nc] in node.children):
                    dfs(nr, nc, node.children[board[nr][nc]], path + board[nr][nc])

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in self.trie.root.children:
                    dfs(r, c,self.trie.root.children[board[r][c]], board[r][c])
        return list(found)