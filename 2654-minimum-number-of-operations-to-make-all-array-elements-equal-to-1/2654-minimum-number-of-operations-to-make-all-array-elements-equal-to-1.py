import math
from functools import reduce
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        if reduce(math.gcd,nums)!=1:
            return -1
        if 1 in nums:
            return len(nums)-nums.count(1)
        mini = n

        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    mini = min(mini, j - i + 1)
                    break
        return (mini-1)+(n-1)
