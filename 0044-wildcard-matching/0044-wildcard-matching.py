class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p1=p2=0
        m,n=len(s),len(p)
        dp=[[None]*(n+1) for i in range(m+1)]

        def fun(p1,p2):
            if p1==m and p2==n:
                dp[p1][p2]=True
                return dp[p1][p2]

            if p2==n:
                dp[p1][p2]=False
                return dp[p1][p2]

            if p1==m:
                if p[p2]=='*':
                    return fun(p1,p2+1)
                return False

            if dp[p1][p2] is not None:
                return dp[p1][p2]

            valid=(s[p1]==p[p2] or p[p2] in ['?','*'])

            if p[p2]=='*':
                dp[p1][p2]=fun(p1,p2+1) or fun(p1+1,p2)
                return dp[p1][p2]

            if valid:
                dp[p1][p2]=fun(p1+1,p2+1)
                return dp[p1][p2]

            dp[p1][p2]=False
            return dp[p1][p2]

        return fun(0,0)