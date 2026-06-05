for t in range(int(input())):
    a,b=map(int,input().split())
    arr=[True]*(b-a+1)
    for i in range(2,int(b**0.5)+1):
        start=max(i*i,((a+i-1)//i)*i)
        for j in range(start,b+1,i):
            arr[j-a]=False
    for i in range(a,b+1):
        if i!=1 and arr[i-a]==True:
            print(i)
