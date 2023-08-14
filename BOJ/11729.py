def func(N,a,b,c):
    if N==1:
        print(a,c)
    else:
        func(N-1,a,c,b)
        print(a, c)
        func(N-1,b,a,c)
    sum=2**N-1
    print(sum)


N=int(input())
print(2**N-1)

func(N,1,2,3)