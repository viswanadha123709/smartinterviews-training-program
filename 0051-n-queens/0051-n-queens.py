class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]

        def valid(row,col,board):
            for i in range(n):
                if board[row][i]=='Q' or board[i][col]=='Q':
                    return False
            i,j=row,col
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i,j=row,col
            while i<n and j<n:
                if board[i][j]=='Q':
                    return False
                i+=1
                j+=1
            i,j=row,col
            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            i,j=row,col
            while i<n and j>=0:
                if board[i][j]=='Q':
                    return False
                i+=1
                j-=1
            return True


        def fun(col,board):
            if col==n:
                ans.append([''.join(i) for i in board])
                return 
            for i in range(n):
                if valid(i,col,board):
                    board[i][col]="Q"
                    fun(col+1,board)
                    board[i][col]='.'
        fun(0,[['.']*n for i in range(n)])
        return ans