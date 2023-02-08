def Counting_sort(A, B, K):
    # A[] = 입력된 배열(0 to k(문제 조건))
    # B[] = 정렬된 배열
    # K[] = 카운트 배열

    C = [0] * k

    for i in range(0, len(A)):
        C[A[i]] += 1
    
    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]