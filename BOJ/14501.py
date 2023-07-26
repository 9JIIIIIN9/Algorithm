import sys
N=int(input())

sign = [list(map(int,sys.stdin.readline().split()))for i in range(N)]

dp = [0 for i in range(N+1)]
for i in range(N):
    for j in range(i+sign[i][0],N+1):    #상담가능 날짜
        if dp[j]<dp[i]+sign[i][1]:
            dp[j]=dp[i]+sign[i][1]  # 최대 수익 담기

print(dp[-1])