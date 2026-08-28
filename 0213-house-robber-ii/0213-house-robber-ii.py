class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp1=[nums[0]]
        dp2=[nums[-1]]
        if n>2:
            dp1.append(max(nums[0],nums[1]))
            dp2.append(max(nums[-1],nums[-2]))
        for i in range(2,n-1):
            dp1.append(max(dp1[-1],nums[i]+dp1[-2]))
            dp2.append(max(dp2[-1],nums[n-i-1]+dp2[-2]))
        return max(dp1[-1],dp2[-1])