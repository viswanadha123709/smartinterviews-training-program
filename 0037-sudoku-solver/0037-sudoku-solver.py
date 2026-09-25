class Solution:
    def solveSudoku(self,board:list[list[str]])->None:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        d={}
        for i in range(3):
            d[i]={}
            for j in range(3):
                d[i][j]=set()

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    val=int(board[i][j])
                    row[i].add(val)
                    col[j].add(val)
                    d[i//3][j//3].add(val)

        def valid(i,j,val):
            if val in row[i]:
                return False
            if val in col[j]:
                return False
            if val in d[i//3][j//3]:
                return False
            return True

        def backtrack(idx):
            if idx==81:
                return True

            r=idx//9
            c=idx%9

            if board[r][c]!='.':
                return backtrack(idx+1)

            for i in range(1,10):
                if valid(r,c,i):
                    board[r][c]=str(i)
                    row[r].add(i)
                    col[c].add(i)
                    d[r//3][c//3].add(i)

                    if backtrack(idx+1):
                        return True

                    board[r][c]='.'
                    row[r].remove(i)
                    col[c].remove(i)
                    d[r//3][c//3].remove(i)

            return False

        backtrack(0)