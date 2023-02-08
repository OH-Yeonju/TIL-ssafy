# 순차 검색
def sequentialSearch1(a, n, key):
    i = 0
    while i<n and a[i]!=key:
        i += 1
    if i<n:
        return i
    else:
        return -1


def sequentialSearch2(a, n, key):
    i = 0
    while i<n and a[i]<key:
        i += 1
    if i<n and a[i]==key: # 검색 성공한 경우
        return i
    else:
        return -1 # key값 없어 검색 실패한 경우


# 이진 검색
def binarySearch(a, N, key): #N개의 원소
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return True
        elif a[middle] > key:
            end = middle-1
        else:
            start = middle + 1
    return False # 검색 실패

# 선택 정렬
def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

# 셀렉션 알고리즘(k번째로 작은 원소를 찾는 알고리즘)
def select(arr, N):
    for i in range(0, k):
        minIdx = i
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr[k-1]