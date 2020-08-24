# selection sort
# 맨 앞에 있는 숫자를 기준값으로 생각, 나머지 값중 제일 작은 값을 앞으로 보냄
def selection_sort(a):
    for i in range(len(a) - 1) :
        min_idx = i
        for j in range(i + 1, len(a)) :
            if a[min_idx] > a[j] :
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

list = [5,2,4,1,3]
selection_sort(list)
print(list)