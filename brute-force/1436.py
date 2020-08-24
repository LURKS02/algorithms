N = int(input())
list = []

for i in range(2666800) :
    num = str(i)
    for j in range(len(num) - 2):
        if (num[j] == '6' and num[j+1] == '6' and num[j+2] == '6') :
            list.append(i)
            break
print(list[N - 1])