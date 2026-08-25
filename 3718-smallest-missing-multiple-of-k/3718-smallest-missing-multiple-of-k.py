class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp=set(nums)
        for i in range(1,105):
            if i*k not in temp:
                return i*k
        return i*k

        