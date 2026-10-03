class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans=[]
        def check(s):
            return s==s[::-1]
        def backtrack(idx,curr):
            if idx==len(s):
                ans.append(curr)
                return
            for i in range(idx,len(s)):
                if check(s[idx:i+1]):
                    temp=curr.copy()
                    temp.append(s[idx:i+1])
                    backtrack(i+1,temp)
        
        backtrack(0,[])
        return ans
            