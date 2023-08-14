#종이의 갯수


#while
#0-2, 2-4, 5-8
def func(h,v,N):
    arr = A[h][v]
    for i in range(h,h+N):
        for j in range(v,v+N):




    if arr==-1:
        count[0]+=1
    elif arr==0:
        count[1]+=1
    else:
        count[2]+=1

N=int(input())
A=[list(map(int,input().split()))for _ in range(N)]
#-1 0 1 갯수
count=[0,0,0]
