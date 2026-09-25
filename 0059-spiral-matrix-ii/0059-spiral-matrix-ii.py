class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans=[[0]*n for i in range(n)]
        count=1
        top=0
        left=0
        right=n-1
        bottom=n-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans[top][i]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                ans[i][right]=count
                count+=1
            right-=1
            if left<=right:
                for i in range(right,left-1,-1):
                    ans[bottom][i]=count
                    count+=1
                bottom-=1
            if top<=bottom:
                for i in range(bottom,top-1,-1):
                    ans[i][left]=count
                    count+=1
                left+=1
        return ans