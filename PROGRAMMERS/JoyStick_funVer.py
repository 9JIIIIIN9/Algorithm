def solution(name):
    count = 0
    for i in range(len(a)):
        if a[i] == 'A':
            continue
            #알파벳이 A거나, 마지막 알파벳이 아니면 이동했다고 생각하고 count+1한 것.
        elif ord(a[i]) - ord("A") <= 12:    #B-M   A의 아스키 : 65, M의 아스키 : 77
            if i != len(a) - 1:      #마지막 알파벳인지?
                count += 1           #아니라면 +1(이동횟수)
            count += (ord(a[i]) - ord("A"))   #아스키 코드값(J기준 74-65=9 담김)

        else:                       #N-Z 일 때
            if i != len(a) - 1:     #
                count += 1          #이동횟수+1

            count += (91 - ord(a[i]))   #Z의 아스키 코드가 90이므로 91- 하면 A에서 Z로 이동한 수 포함하게 되는 것
    return count


a = []
a = input()
print(solution(a))


#반례 : AAB



# 나는 알파벳이 A거나 마지막 글자가 아니면 count+=1을 하도록 짰는데 그렇게 하니까 AAB 일 때가 안되네..
