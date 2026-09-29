class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res=[]

        def backtrack(index,string):
            if index==len(digits):
                res.append(string)
                return
            letters=d[digits[index]]

            for i in letters:
                backtrack(index+1,string+i)
        
        backtrack(0,"")
        return res
            

        
        