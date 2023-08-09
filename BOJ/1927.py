#최소 힙 "틀렸습니다"

import heapq
import sys
n=int(input("입력 :"))
li=[]
for i in range(n):
    tem=int(sys.stdin.readline())   #자연수 값 넣기

    if tem!=0:   #0아니면 배열에 tem값 넣기
        heapq.heappush(li,tem)

    else:
        if len(li)!=0:    # 작은 값 출력하기
            print(heapq.heappop(li))
        else:    #값이 없으면 0 출력
            print(0)
