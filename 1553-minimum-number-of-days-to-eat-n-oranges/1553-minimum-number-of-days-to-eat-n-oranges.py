from functools import lru_cache
class Solution:
    def minDays(self, n: int) -> int:
        dp={}
        @lru_cache
        def check(x):
            if x==0:
                return 0
            if x==1:
                return 1
            dp[x]=1+min(x%2+check(x//2),x%3+check(x//3))
            return dp[x]

        return check(n)