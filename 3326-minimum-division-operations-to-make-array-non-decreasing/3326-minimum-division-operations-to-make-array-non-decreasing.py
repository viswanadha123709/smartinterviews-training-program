class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def divisor(n):
            maxi=0
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    maxi=max(i,n//i)
                    return maxi
            return n

        ans=0
        n=len(nums)
        for i in range(n-2,-1,-1):
            val=nums[i]
            while val>nums[i+1]:
                val//=divisor(val)
                if val==1:
                    return -1
                nums[i]=val
                ans+=1
        return ans
