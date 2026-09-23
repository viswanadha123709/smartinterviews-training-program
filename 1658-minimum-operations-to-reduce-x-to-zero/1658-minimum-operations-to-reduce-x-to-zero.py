from functools import lru_cache
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        total=sum(nums)
        if total<x:
            return -1
        target=total-x
        ans=-1
        curr=0
        count=0
        left=0
        for i in range(n):
            curr+=nums[i]
            count+=1
            while left<=i and curr>target:
                curr-=nums[left]
                left+=1
                count-=1
            if curr==target:
                ans=max(ans,count)
        return -1 if ans == -1 else n - ans


                
