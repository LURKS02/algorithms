# Sorting Algorithms
## 선택정렬 (selection sort)

![SelectionSort_Avg_case](https://user-images.githubusercontent.com/63408930/91028860-0636cb00-e639-11ea-9a04-44ac3611a9ab.gif)
```python
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
```
* 안쪽 for문에서 배열의 최솟값을 찾아 바깥쪽 for문의 첫번째 값과 swap
* 이중 for문으로 시간복잡도 = O(n^2)
* stable하지 않음

***
## 삽입정렬 (insertion sort)

![insertionSort](https://user-images.githubusercontent.com/63408930/91029071-472edf80-e639-11ea-9117-872995ab17ef.gif)
```python
def insertion_sort(a):
    for i in range(1, len(a)):
        idx = i
        for j in range(i - 1, -1, -1) :
            if a[idx] < a[j] :
                a[idx], a[j] = a[j], a[idx]
                idx = j
            else :
                # 새로 삽입하려는 요소가 정렬된 리스트의 마지막 요소보다 크다면 비교할 필요 없음
                break

list = [2,8,9,4,10]
insertion_sort(list)
print(list)
```
* 배열의 요소를 정렬된 부분의 값들과 비교하며 자리를 찾아가는 방식
* 시간복잡도 = O(n^2)
* 이미 데이터가 정렬되었을때는 바로 옆자리 값만 비교하므로 상수 번의 시간복잡도 O(n)

***
## 버블정렬 (bubble sort)

![BubbleSort_Avg_case](https://user-images.githubusercontent.com/63408930/91028588-a6d8bb00-e638-11ea-9b82-a3e2f1e9264f.gif)
```python
def bubble_sort(a):
    for i in range(len(a) - 1) :
        for j in range(len(a) - 1, i, -1) :
            if a[j - 1] > a[j] :
                a[j], a[j - 1] = a[j - 1], a[j]

list = [5, 4, 3, 2, 1]
bubble_sort(list)
print(list)
```
* 인접 요소들을 서로 반복적으로 교환하는 방식
* 시간복잡도 = O(n^2)

***
## 퀵정렬 (quick sort)

![quick-sort-animation](https://user-images.githubusercontent.com/63408930/91142357-9afa0100-e6eb-11ea-9335-892cf62eccf1.gif)
```python
def quick_sort(a):
    if len(a) <= 1 :
        return a
    else :
        pivot = a[0]
        less = [x for x in a[1:] if x <= pivot]
        greater = [x for x in a[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

list = [3,2,5,1,4]
print(quick_sort(list))
```
* pivot을 기준으로 분할(partition) 진행
* 시간복잡도 = O(nlogn)
* 최악의 경우 - pivot 선정시 최솟값 또는 최댓값이 선정되어 좌우 한쪽이 없거나 1뿐인 배열 (시간복잡도 = O(n^2))
