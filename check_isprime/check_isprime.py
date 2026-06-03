for testcase in range(int(input())):
    n=int(input())
    if n<=1:
        print("No")
        continue
    if n in [2,3]:
        print("Yes")
        continue
    if n%2==0:
        print("No")
        continue

    k=0
    m=n-1
    while(m%2==0):
        m//=2
        k+=1
    a=2
    x=pow(a,m,n)
    prime=False
    if x==n-1 or x==1:
        print("Yes")
        continue
    for i in range(k):
        x=pow(x,a,n)
        if x==n-1:
            prime=True
            break
        if x==1:
            prime=False
            break         
    if prime:
        print("Yes")
    else:
        print("No")
