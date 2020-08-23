'''
EOF : end of file
예외처리 이용
'''

while True :
    try :
        A, B = map(int, input().split())
        print(A + B)
    except :
        break
