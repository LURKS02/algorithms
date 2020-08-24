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

