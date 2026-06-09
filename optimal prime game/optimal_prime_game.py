maxi=10**4
arr=[True]*(maxi+1)
primes=[]
arr[0]=arr[1]=False
for i in range(2,int(maxi)+1):
    if arr[i]==True:
        primes.append(i)
        for j in range(i*i,maxi+1,i):
            arr[j]=False
    else:
        for j in primes:
            if arr[i-j]==False:
                arr[i]=True
for t in range(int(input())):
    n=int(input())
    if arr[n]==True:
        print("First")
    else:
        print("Second")
