from sortedcontainers import SortedList
from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        h=SortedList()
        n=len(envelopes)
        ans=0
        for i in range(n):
            idx=h.bisect_left(envelopes[i][1])
            ans=max(ans,idx+1)
            if idx==len(h):
                h.add(envelopes[i][1])
                continue
            h.pop(idx)
            h.add(envelopes[i][1])        
        return ans


