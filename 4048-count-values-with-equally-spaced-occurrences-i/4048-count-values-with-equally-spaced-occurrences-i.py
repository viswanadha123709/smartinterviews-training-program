class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n=len(nums)
        ans=0
        d={}
        for i in range(n):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]]=[i]

        for a,b in d.items():
            if len(b)==3:
                if b[1]-b[0]==b[2]-b[1]:
                    ans+=1
        return ans