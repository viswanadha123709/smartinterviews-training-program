class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans=[]
        def backtrack(curr,val,visited):
            if len(curr)==k:
                ans.append(curr.copy())
                return
            if val==n+1:
                return
            for i in range(val,n+1):
                if i not in visited:
                    visited.add(i)
                    curr.append(i)
                    backtrack(curr,i+1,visited)
                    visited.remove(i)
                    curr.pop()
        backtrack([],1,set())
        return ans