mod=1000000007
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=1
    if n>3000:
        print(0)
        continue
    for i in range(n):
        for j in range(i+1,n):
            p=(arr[i]^arr[j])%mod
            ans=(ans*p)%mod
    print(ans)
    
