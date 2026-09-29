
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        dp={}
        def backtrack(row,col,visited,bal):    
            if grid[row][col]=='(':
                bal+=1
            else:
                bal-=1
            if (row,col,bal) in dp:
                return dp[(row,col,bal)]
            if bal<0:
                return False
            if row==m-1 and col==n-1:
                return bal==0
            visited[row][col]=1
            down=right=False
            if row<m-1 and visited[row+1][col]==0:
                down=backtrack(row+1,col,visited,bal)
            if col<n-1 and visited[row][col+1]==0:
                right=backtrack(row,col+1,visited,bal)
            visited[row][col]=0
            dp[(row,col,bal)]=down or right
            return down or right
        
        return backtrack(0,0,[[0]*n for i in range(m)],0)
                
            
            
