class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root

        for c in word:
            if c not in root.children:
                root.children[c] = Node()
            root = root.children[c]

        root.word = True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.rows = len(board)
        self.cols = len(board[0])
        self.ans = {}

        for word in words:
            self.trie.insert(word)

        def dfs(board, i, j, path, root):
            c = board[i][j]

            root = root.children.get(c)
            if root is None:
                return

            path = path + [c]
            board[i][j] = None

            if root.word:
                word = ''.join(path)
                self.ans[word] = True

            if j + 1 < self.cols and board[i][j+1]:
                dfs(board, i, j+1, path, root)

            if j - 1 >= 0 and board[i][j-1]:
                dfs(board, i, j-1, path, root)

            if i + 1 < self.rows and board[i+1][j]:
                dfs(board, i+1, j, path, root)

            if i - 1 >= 0 and board[i-1][j]:
                dfs(board, i-1, j, path, root)
            
            board[i][j] = c
        
        for i in range(self.rows):
            for j in range(self.cols):
                dfs(board, i, j, [], self.trie.root)

        return self.ans.keys()
