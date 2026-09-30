from sortedcontainers import SortedList
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        s=SortedList()
        for i in range(n):
            idx=s.bisect_left(nums[i])
            ans=max(ans,idx+1)
            if idx==len(s):
                s.add(nums[i])
                continue
            s.pop(idx)
            s.add(nums[i])
        return ans
            