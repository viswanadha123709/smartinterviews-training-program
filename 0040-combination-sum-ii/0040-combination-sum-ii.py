class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        n=len(candidates)
        candidates.sort()
        def backtrack(curr,summ,idx):
            if summ==target:
                ans.append(curr.copy())
                return True
            if idx==n+1 or summ>target:
                return False
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(curr,summ+candidates[i],i+1)  
                curr.pop()
            return True
        backtrack([],0,0)
        return ans




