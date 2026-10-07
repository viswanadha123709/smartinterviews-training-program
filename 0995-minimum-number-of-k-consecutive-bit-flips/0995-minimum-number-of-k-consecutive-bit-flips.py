class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n=len(nums)
        d=[0]*(n+1)
        i=0
        ans=0
        prefix=0
        while i<n:
            prefix+=d[i]
            if prefix%2!=0:
                nums[i]=1-nums[i]
            if nums[i]==0:
                if i+k>n:
                    return -1
                prefix+=1
                ans+=1
                d[i+k]-=1
            i+=1
        
        return ans
        

        
