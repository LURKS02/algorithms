N = int(input())

max = -1111111
min = 1111111
list = list(map(int,input().split()))
for i in range(N):
    if (max < list[i]) : max = list[i]
    if (min > list[i]) : min = list[i]
print("%d %d"%(min,max))
