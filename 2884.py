A, B = map(int, input().split())
if B < 45 :
    A -= 1
    B += 15
    if A < 0 :
        A = 23
else :
    B -= 45
print("%d %d"%(A, B))