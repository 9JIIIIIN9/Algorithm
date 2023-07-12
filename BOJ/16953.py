# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 2를 곱하는 거, 1을 수의 가장 오른쪽에 추가하는 것

i, j = map(int, input().split())
#A,B
count = 0 #횟수
while i < j:
    if j % 2 == 1:   #일의 자리 홀수인지?
        if j % 10 == 1: #일의 자리 1인지?
            j = j // 10  # n정수 몫 담기
            count += 1 # 횟수+1
        else:            #일의 자리가 3,5,7,9인 것
            break        #무시하고 while문

    else:
        j = j / 2    # 일의 자리 짝수이므로 2나눈 값 담기
        count += 1 # 횟수+1

if i == j:  #두 정수가 같아지면 지금까지 횟수 출력
    print(count + 1)
else:
    print(-1) # A>B 이고 A!=B이면 -1 출력


