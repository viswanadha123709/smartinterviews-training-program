import heapq as hq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        dp=[1]
        indexes={}
        for i in primes:
            indexes[i]=0
        while len(dp)<n:
            curr=2**32
            for a,b in indexes.items():
                curr=min(curr,a*dp[b])
            dp.append(curr)
            for a,b in indexes.items():
                if curr==a*dp[b]:
                    indexes[a]+=1
        return dp[-1]