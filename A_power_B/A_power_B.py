for t in range(int(input())):
    a,b=map(int,input().split())
    a=a%(10**9 +7)
    ans=1
    while(b!=0):
        if (b&1)==1:
            ans=ans*a%(10**9 + 7)
        a*=a%(10**9+7)
        b=b>>1
    print(ans)
