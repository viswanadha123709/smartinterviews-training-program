class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def check(a,b):
            if (b[0]<a[2] and b[1]<a[3]) and (b[2]>a[0] and b[3]>a[1]):
                return True
            return False
        
        if check(rec1,rec2) or check(rec2,rec1):
            return True
        return False