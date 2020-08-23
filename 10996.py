def func(A) :
    if A == 1 :
        print("*")
    else :
        for i in range (A*2) :
            if i % 2 == 0 :
                print("* " * ( (A + 1) // 2 ))
            else :
                print(" *" * ( A // 2 ))

A = int(input())
func(A)