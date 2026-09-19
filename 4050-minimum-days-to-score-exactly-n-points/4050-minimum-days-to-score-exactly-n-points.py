class Solution:
    def minDays(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0]=0
        def check(x):
            if x==0:
                return 0
            if dp[x]!=-1:
                return dp[x]
            ans=10**9
            k=1
            while k * (k + 1) // 2 <= x:
                total=k*(k+1)//2
                cost = k + (1 if x - total > 0 else 0)
                ans=min(ans,cost+check(x-total))
                k+=1
            dp[x]=ans
            return ans
        return check(n)