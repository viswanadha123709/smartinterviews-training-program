class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        while len(ans)<numRows:
            curr=ans[-1]
            temp=[]
            temp.append(curr[0])
            for i in range(len(curr)-1):
                temp.append(curr[i]+curr[i+1])
            temp.append(curr[-1])
            ans.append(temp)
            
        return ans
