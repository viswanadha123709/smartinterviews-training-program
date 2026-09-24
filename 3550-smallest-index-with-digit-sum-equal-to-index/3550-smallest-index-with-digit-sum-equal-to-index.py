class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def total(n):
            total=0
            for i in str(n):
                total+=int(i)
            return total
        for i in range(len(nums)):
            if total(nums[i])==i:
                return i
        return -1