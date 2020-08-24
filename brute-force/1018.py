A, B = map(int, input().split())
list = []
for i in range(A) :
    list.append(input())

least = 9999

for i in range(A - 7) :
    for j in range(B - 7) :
        sum = 0
        firststr = 'W'
        for m in range(8) :
            for n in range(8) :
                if m % 2 == 0 :
                    if n % 2 == 0 :
                        if list[i + m][j + n] != firststr :
                            sum += 1
                    else :
                        if list[i + m][j + n] == firststr :
                            sum += 1
                else :
                    if n % 2 == 0 :
                        if list[i + m][j + n] == firststr :
                            sum += 1
                    else :
                        if list[i + m][j + n] != firststr :
                            sum += 1
        if least > sum :
            least = sum

        sum = 0
        firststr = 'B'
        for m in range(8):
            for n in range(8):
                if m % 2 == 0:
                    if n % 2 == 0:
                        if list[i + m][j + n] != firststr:
                            sum += 1
                    else:
                        if list[i + m][j + n] == firststr:
                            sum += 1
                else:
                    if n % 2 == 0:
                        if list[i + m][j + n] == firststr:
                            sum += 1
                    else:
                        if list[i + m][j + n] != firststr:
                            sum += 1
        if least > sum:
            least = sum

print(least)