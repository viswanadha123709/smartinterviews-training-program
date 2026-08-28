maxi=5*10**6
primes=[True]*(maxi+1)
primes[0]=primes[1]=False
for i in range(2,int(maxi**0.5)+1):
    if primes[i]==True:
        for j in range(i*i,maxi+1,i):
            primes[j]=False


class Solution:
    def countPrimes(self, n: int) -> int:
        ans=0
        for i in range(n):
            if primes[i]==True:
                ans+=1
        return ans
        
