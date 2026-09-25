class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        l=len(word)
        n=len(board)
        m=len(board[0])
        def backtrack(idx,row,col,visited):
            visited[row][col]=1
            if board[row][col]!=word[idx]:
                visited[row][col]=0
                return False
            if idx==l-1:
                return True
            if board[row][col]==word[idx]:
                if row>0 and visited[row-1][col]==0:
                    if backtrack(idx+1,row-1,col,visited):
                        return True
                if row<n-1 and visited[row+1][col]==0:
                    if backtrack(idx+1,row+1,col,visited):
                        return True
                if col>0 and visited[row][col-1]==0:
                    if backtrack(idx+1,row,col-1,visited):
                        return True
                if col<m-1 and visited[row][col+1]==0:
                    if backtrack(idx+1,row,col+1,visited):
                        return True
            visited[row][col]=0
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(0,i,j,[[0]*m for i in range(n)]):
                        return True
        return False
        
            