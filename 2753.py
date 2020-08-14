def check(A) :
    if A % 4 == 0 and A % 100 != 0:
         return "1"
    elif A % 400 == 0 :
        return "1"
    else :
        return "0"
print(check(int(input())))