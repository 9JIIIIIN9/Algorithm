#2470 두 용액
#틀렸습니다

# import sys
# import itertools
# num = int(sys.stdin.readline())
# queue=0
# a=list(map(int,input().split()))
#
# print(a)
#
# print(list(map(list,itertools.combinations(a,2))))
# B=list(map(list,itertools.combinations(a,2)))
# print("test : ", B)
# print(len(list(B)))
# for i in range(len(list(B))):   #0-9
#     C = abs(int(B[i][0])+int(B[i][1]))
#     if i==0 or C<queue:
#         queue=C
#     else:
#         continue
#
#
#     # if i==0:
#     #      queue.append(C)
#     # for j in range(len(queue)):
#     #     if C<queue[j]:
#     #         queue.append(C)
#     #         continue
#     # else:
#     #     continue
# print("최소 절댓값 : ",queue)




n = int(input())
arr = sorted(list(map(int, input().split(' '))))
#오름차순 정렬 후 처음과 마지막 원소를 담아
S = 0
E = n-1

ab = abs(arr[S]+arr[E]) #초기화
ans = [arr[S], arr[E]]

while S<E:
    s = arr[S]
    e = arr[E]

    sum = s+e

    #절댓값이 기존 값보다 작으면 그 값을 ab에 넣기
    if abs(sum)<ab:
        print("test:",abs(sum),ab)
        ab = abs(sum)
        final = [S,E]

    if sum<0:
        S+=1
    else:
        E-=1

print(ans[0], ans[1])

#반례
#5 / -99 -98 1 0 96