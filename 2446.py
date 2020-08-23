A = int(input())
for i in range(A):
    print(" "*i, end = "")
    print("*"*(2*A - 1 - 2*i))
for i in range(A - 1, 0, -1):
    print(" "* (i-1), end = "")
    print("*"*(2*A - 1 - 2*(i - 1)))
