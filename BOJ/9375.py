#미완성
#패션왕 신해빈
N=int(input())
for i in range(N):
    A=int(input())
    li={}
    for j in range(A):
        Opt,Category=list(map(str,input().split()))

        #li 안에 종류 있어?
        if Category in li:
            print(li)
        else:
            print(li)



        print(li[Category])
