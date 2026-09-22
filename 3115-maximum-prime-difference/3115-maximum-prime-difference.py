class Solution:
    maxi=100
    arr=[True]*(maxi+1)
    arr[0]=arr[1]=False
    for i in range(2,int(maxi**0.5)+1):
        if arr[i]:
            for j in range(i*i,maxi+1,i):
                arr[j]=False
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n=len(nums)
        p1=0
        p2=0
        for i in range(n):
            if self.arr[nums[i]]:
                p1=i
                break
        for i in range(n-1,-1,-1):
            if self.arr[nums[i]]:
                p2=i
                break
        return p2-p1
        