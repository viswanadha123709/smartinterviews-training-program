def mergesort(arr,low,high):
    mid=(low+high)//2
    if low<high:
        c=0
        c+=mergesort(arr,low,mid)
        c+=mergesort(arr,mid+1,high)
        c+=merge(arr,low,mid,high)
        return c
    else:
        return 0

def merge(arr,low,mid,high):
    p1=low
    p2=mid+1
    temp=[]
    count=0
    while(p1<=mid and p2<=high):
        if arr[p1]<=arr[p2]:
            temp.append(arr[p1])
            p1+=1
        else:
            temp.append(arr[p2])
            count+=mid-p1+1
            p2+=1
    while(p1<=mid):
        temp.append(arr[p1])
        p1+=1
    while(p2<=high):
        temp.append(arr[p2])
        p2+=1
    arr[low:high+1]=temp
    return count

for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c=mergesort(arr,0,n-1)
    print(c)
