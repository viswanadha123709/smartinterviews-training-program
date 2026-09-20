class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        def check(p1,p2):
            if p2 == n:
                return p1 == m
            if p1==m:
                if p2==n:
                    return True
                if p2+1<n and p[p2+1]=='*':
                    return check(p1, p2 + 2)
                return False

            valid=s[p1]==p[p2] or p[p2]=='.'

            if p2+1<n and p[p2+1]=='*':
                return check(p1,p2+2) or (valid and check(p1+1,p2))
            
            if valid:
                return check(p1+1,p2+1)
            return False
        
        return check(0,0)
        
            
            
