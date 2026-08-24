class Solution:
    def sumGame(self, num: str) -> bool:
        l=0
        r=0
        lq=rq=0
        n=len(num)
        m=0
        target=0
        for i in range(n//2):
            if num[i]!='?':
                l+=int(num[i])
            else:
                lq+=1
        for i in range(n//2,n):
            if num[i]!='?':
                r+=int(num[i])
            else:
                rq+=1
        
        return 2 * (l - r) != 9 * (rq - lq)

        
        


