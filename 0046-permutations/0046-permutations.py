class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        def permi(curr,visited):
            if curr and len(curr)==n:
                ans.append(curr[:])
                return
            for i in range(n):
                if visited[i]==0:
                    visited[i]=1
                    curr.append(nums[i])
                    permi(curr,visited)
                    curr.pop()
                    visited[i]=0
        curr=[]
        permi(curr,[0]*n)
        return ans