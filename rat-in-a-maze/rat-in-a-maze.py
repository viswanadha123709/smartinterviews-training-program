class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        ans=[]
        n=len(maze)
        if maze[0][0]==0 or maze[n-1][n-1]==0:
            return ans
            
            
        def fun(curr,row,col,visited):
            visited[row][col]=1

            if row==n-1 and col==n-1:
                ans.append(curr)
                visited[row][col]=0
                return
            if row<n-1 and maze[row+1][col]==1 and visited[row+1][col]==0:
                fun(curr+"D",row+1,col,visited)
            if col>0 and maze[row][col-1]==1 and visited[row][col-1]==0:
                fun(curr+"L",row,col-1,visited)
            if col<n-1 and maze[row][col+1]==1 and visited[row][col+1]==0:
                fun(curr+"R",row,col+1,visited)
            if row>0 and maze[row-1][col]==1 and visited[row-1][col]==0:
                fun(curr+"U",row-1,col,visited)
            visited[row][col]=0
            

        fun("",0,0,[[0]*n for i in range(n)])
        return ans
