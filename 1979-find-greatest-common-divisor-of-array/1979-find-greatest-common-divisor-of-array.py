class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if a+b in [a,b]:
                return a+b
            return gcd(b,a%b)
        return gcd(max(nums),min(nums))
