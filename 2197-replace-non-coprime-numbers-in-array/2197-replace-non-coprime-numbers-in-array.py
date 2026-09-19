import math
class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack=[nums[0]]
        for i in nums[1:]:
            curr=i
            while stack and math.gcd(curr,stack[-1])>1:
                x=stack.pop()
                curr=(x*curr)//math.gcd(x,curr)
            else:
                stack.append(curr)
        return stack
        