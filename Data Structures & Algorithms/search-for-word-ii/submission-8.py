class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        DIRS = ((0, 1), (1, 0), (-1, 0), (0, -1))
        path = set()
        res = []
        cur = []

        def dfs(r, c, node):
            if node.isWord:
                res.append(''.join(cur))
                node.isWord = False
            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c
                if (not(0 <= nr < ROWS and 0 <= nc < COLS)
                 or (nr, nc) in path):
                    continue
                if board[nr][nc] not in node.children:
                    continue
                path.add((nr, nc))
                cur.append(board[nr][nc])
                dfs(nr, nc, node.children[board[nr][nc]])
                cur.pop()
                path.remove((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie.root.children:
                    cur = [board[r][c]]
                    path.add((r, c))
                    dfs(r, c, trie.root.children[board[r][c]])
                    path.remove((r, c))

        return res