n=int(input("n="))
arr = list(map(int,input().split()))
count=0

while sum(arr)>0:
    point =0
    for i in range(len(arr)):
        if arr[i]==0 or arr[i]==1 or arr[i]%2!=0:  #2로 나눠지지 않으면
            if arr[i]==0:  #이미 0이 되어버렸으면 다음 친구 확인하러
                continue
            else:  #홀수이면 -1 하고 count+
                arr[i]-=1
                count+=1
            point=1   #값이 홀수이거나 1이거나 0일때
    if point ==0:  #값이 짝수일때
        for i in range(n):
            arr[i]//=2
        count+=1
print(count)
