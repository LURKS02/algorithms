max = 0
maxind = -1
for i in range(9) :
    num = int(input())
    if max < num :
        max = num
        maxind = i + 1

print(max)
print(maxind)