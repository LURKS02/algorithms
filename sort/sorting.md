# Sorting Algorithms
## 선택정렬 (selection sort)

![select](https://user-images.githubusercontent.com/63408930/91021692-0fbb3580-e62f-11ea-85cc-d8c53389f84b.gif)
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

![insert](https://user-images.githubusercontent.com/63408930/91026064-37ad9780-e635-11ea-890c-6cd0ea098f4e.gif)
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
