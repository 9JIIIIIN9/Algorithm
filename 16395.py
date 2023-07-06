n,k = map(int,input().split())
#print(n,k)

a=[0 for i in range(10)]


for i in range(n+1):
    b=[0 for i in range(10)]
    for j in range(i+1):
        if j==0 or i==0 or j==i:
            b.append(1)
            break
        else:
            b.append(a[i-1][j-1]+a[i-1][j])
    a.append(b)
print(a[n-1][k-1])
