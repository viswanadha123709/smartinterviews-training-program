class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        ans=0
        d={}
        bool={}
        visited=set()
        for i in nums:
            d[i]=[]
            bool[i]=True
        for i in range(len(nums)):
            if d[nums[i]]==[]:
                d[nums[i]]=[i]
            elif len(d[nums[i]])==1:
                d[nums[i]].append(i)
            else:
                diff=d[nums[i]][-1]-d[nums[i]][-2]
                d[nums[i]].append(i)
                if d[nums[i]][-1]-d[nums[i]][-2]!=diff:
                    bool[nums[i]]=False
        for a,b in d.items():
            if len(b)<3:
                bool[a]=False
        for i in nums:
            if bool[i] and i not in visited:
                ans+=1
            visited.add(i)
        return ans
                
            