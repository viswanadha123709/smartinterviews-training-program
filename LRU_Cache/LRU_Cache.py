import sys
input=sys.stdin.readline
for t in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    hm1={}
    hm2={}
    p1=0
    for i in range(n):
        if hm1.get(arr[i])==None:
            if len(hm1)==k:
                while(hm2.get(p1)==None):
                    p1+=1
                hm1.pop(hm2[p1])
                hm2.pop(p1)
                p1+=1
            hm1[arr[i]]=i
            hm2[i]=arr[i]
        else:
            hm2.pop(hm1[arr[i]])
            hm2[i]=arr[i]
            hm1[arr[i]]=i
    for i in range(p1,n):
        if hm2.get(i)!=None:
            print(hm2[i],end=" ")
    print()
