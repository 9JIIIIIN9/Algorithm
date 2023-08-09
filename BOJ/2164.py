#카드2
#시간 초과

import sys
N=int(sys.stdin.readline())
li=list(range(1,N+1))
while len(li)>1:
    li.pop(0)
    box=li.pop(0)
    li.append(box)
print(li.pop(0))

