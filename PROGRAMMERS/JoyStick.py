a = []
a = input()
count = 0
for i in range(len(a)):
    if a[i] == 'A':
        continue
    elif ord(a[i]) - ord("A") <= 12:
        if i != len(a) - 1:
            count += 1
        count += (ord(a[i]) - ord("A"))
        print("앞에서 : ", count)

    else:
        if i != len(a) - 1:
            count += 1

        count += (91 - ord(a[i]))
        print("뒤에 : ", count)


print(count)