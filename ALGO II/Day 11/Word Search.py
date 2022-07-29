class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                ptr = 0
                used = set()
                stack = [(i,j,0,False)]
                while stack:
                    c, d, ptr, backtrack = stack.pop()
                    if backtrack:
                        used.remove((c,d))
                        continue
                    if board[c][d] == word[ptr]:
                        if ptr == len(word) - 1: return True # terminate if word is found
                        used.add((c,d)) # mark visited node
                        stack.append((c,d,ptr,True)) # append backtracking node
                        dp = [[c + 1, d], [c, d + 1], [c, d - 1], [c - 1, d]]
                        for a, b in dp:
                            if 0 <= a < len(board) and 0 <= b < len(board[0]) and (a,b) not in used:
                                stack.append((a, b, ptr + 1, False))
        return False