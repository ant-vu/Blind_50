from functools import reduce
from collections import defaultdict
class Solution:
    def findWords(self, board, words):
        self.board = board
        self.row_limit = len(board)
        self.col_limit = len(board[0])
        Trie = {}
        for word in words:
            t = Trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c] 
            t['#'] = word
        res = []
        for i in range(self.row_limit):
            for j in range(self.col_limit):
                self.dfs(Trie, i, j, res)
        return list(set(res))
    def dfs(self, trie, i, j, res):
        if '#' in trie:
            res.append(trie['#'])
            del trie['#']
            if not trie:
                return True
        if i < 0 or j < 0 or i >= self.row_limit or j >= self.col_limit or self.board[i][j] not in trie:
            return False
        tmp = self.board[i][j]
        self.board[i][j] = '@'
        value = self.dfs(trie[tmp],i+1, j, res)
        if value:
            del trie[tmp]
            self.board[i][j] = tmp
            if not trie: 
                return True
            else:
                return False
        value = self.dfs(trie[tmp], i-1, j, res)
        if value:
            del trie[tmp]
            self.board[i][j] = tmp
            if not trie: 
                return True
            else:
                return False
        value = self.dfs(trie[tmp], i, j-1, res)
        if value:
            del trie[tmp]
            self.board[i][j] = tmp
            if not trie: 
                return True
            else:
                return False
        value = self.dfs(trie[tmp], i, j+1, res)
        if value:
            del trie[tmp]
            self.board[i][j] = tmp
            if not trie: 
                return True
            else:
                return False
        self.board[i][j] = tmp
        return False
