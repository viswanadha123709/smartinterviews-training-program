class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        from math import gcd

        def lcm(x,y):
            return x//gcd(x,y)*y

        def find(x,arr):
            ans=0
            for i in range(1,8):
                count=0
                prod=1
                for j in range(3):
                    if (i>>j)&1:
                        prod=lcm(prod,arr[j])
                        count+=1
                if count&1:
                    ans+=(x//prod)
                else:
                    ans-=(x//prod)
            return ans

        p1=1
        p2=10**18
        while p1<p2:
            mid=(p1+p2)//2
            if find(mid,[a,b,c])>=n:
                p2=mid
            else:
                p1=mid+1
        return p1


