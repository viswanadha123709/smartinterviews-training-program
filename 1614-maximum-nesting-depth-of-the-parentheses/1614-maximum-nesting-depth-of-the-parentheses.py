class Solution:
    def maxDepth(self, s: str) -> int:
        stack=0
        ans=0
        for i in s:
            if i=='(':
                stack+=1
            elif i==')':
                stack-=1
            ans=max(ans,stack)
        return ans

        

        