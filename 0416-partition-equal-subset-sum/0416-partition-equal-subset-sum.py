from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total&1:
            return False
        n=len(nums)
        target=total//2
        dp=[False]*(target+1)
        dp[0]=True
        for i in nums:
            for j in range(target,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        return dp[target]
        