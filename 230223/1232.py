def cal(n1, n2, i):  # 특수문자 계산
    if i == '+':
        return n1 + n2
    if i == '-':
        return n1 - n2
    if i == '*':
        return n1 * n2
    if i == '/':
        return int(n1 / n2)


for tc in range(1, 10+1):
    N = int(input())
    lst = [0] * (N+1)   # 연산자들과 숫자들이 들어가는 리스트
    c1 = [0] * (N+1)    # 각 인덱스를 부모로 가지는 자식 노드들 넣어줄 리스트
    c2 = [0] * (N+1)
    for i in range(N):
        root = list(input().split())
        if len(root) == 4:        # 연산자일시 무조건 4개 입력됨
            lst[int(root[0])] = root[1]    # 인덱스에 맞게 연산자 넣어줌
            for i in range(2, 4):          # 뒤 번호 두개는 연결된 자식 노드들
                if c1[int(root[0])] == 0:  # 채워져있지 않다면 채움
                    c1[int(root[0])] = int(root[2])
                else:                      # 채워진 상태라면 다음 리스트 채움
                    c2[int(root[0])] = int(root[3])
        if len(root) == 2:    # 잎 노드일시 숫자만 입력됨
            lst[int(root[0])] = int(root[1])


    for i in range(N, 0, -1):    # 아래쪽 노드부터 올라오면서
        if lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or lst[i] == '/':
            lst[i] = cal(lst[c1[i]], lst[c2[i]], lst[i])

    print(f'#{tc} {lst[1]}')

