class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        def permi(curr,bit):
            if curr and len(curr)==n:
                ans.append(curr[:])
                return
            for i in range(n):
                if (bit>>i)&1==0:
                    bit|=(1<<i)
                    curr.append(nums[i])
                    permi(curr,bit)
                    curr.pop()
                    bit^=(1<<i)
        curr=[]
        permi(curr,0)
        return ans