class Solution:
    def primePalindrome(self, n: int) -> int:

        def is_palindrome(x):
            return str(x) == str(x)[::-1]
        
        def is_prime(n):
            if n < 2:
                return False
            if n in [2,3]:
                return True
            if n%2==0:
                return False
            m=n-1
            d=0
            while m%2==0:
                d+=1
                m//=2
            x=pow(2,m,n)
            if x==n-1 or x==1:
                return True
            for i in range(d):
                x=pow(x,2,n)
                if x==n-1:
                    return True
                if x==1:
                    return False
            
        
        while True:
            if is_palindrome(n) and is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8
