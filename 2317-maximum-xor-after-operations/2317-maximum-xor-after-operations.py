class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans=0
        for bit in range(31):
            unsetbit=0
            setbit=0
            for i in nums:
                if i&(1<<bit):
                    setbit+=1
            if setbit:
                ans|=(1<<bit)
        return ans
