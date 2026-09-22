class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        maxi=1000
        spf=[i for i in range(maxi+1)]
        for i in range(2,int(maxi**0.5)+1):
            if spf[i]==i:
                for j in range(i*i,maxi+1,i):
                    if spf[j]==j:
                        spf[j]=i
        temp=set()
        for i in nums:
            while i>1:
                fact=spf[i]
                while i%fact==0:
                    i//=fact
                temp.add(fact)
        return len(temp)



