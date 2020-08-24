cardNum, maxNum = map(int, input().split())
ansNum = 0

list = list(map(int, input().split()))

for i in range (cardNum) :
    for j in range(i + 1, cardNum) :
        for k in range(j + 1, cardNum) :
            case = list[i] + list[j] + list[k]
            if case <= maxNum and case > ansNum :
                ansNum = case

print(ansNum)
