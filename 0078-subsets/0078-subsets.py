class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(2**(len(nums))):
            temp=[]
            for j in range(len(nums)):
                if (i>>j)&1:
                    temp.append(nums[j])
            ans.append(temp)
        return ans