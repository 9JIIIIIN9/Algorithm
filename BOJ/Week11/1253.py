#1253 좋아
#시간 초과

import sys
N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
b=[]
count=0
for i in range(0,N-1): #0-3
    for j in range(1,N):
        c=arr[i]+arr[j]
        if c in arr:
            #본인은 해당이 안되는거잖아,,
            if c not in b:
                b.append(c)
                count+=1

print(count)

#반례
#입력 : 3 / 0 0 1
#출력 : 2
#답 : 0
