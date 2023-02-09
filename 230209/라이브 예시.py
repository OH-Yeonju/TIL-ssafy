p = 'aba' # 찾을 패턴
t = 'aabaababa' # 전체 문장
M = len(p)
N = len(t)

def bf(p, t, N, M):
    i = 0 # t에서의 비교위치
    j = 0 # p에서의 비교위치
    while i < N and j < M: # 비교할 문장이 남아있고 패턴을 찾기 전이면
        if t[i] != p[j]:   # 서로 다른 글자를 만나면
            i -= j         # 비교를 시작한 위치로
            j = -1         # 패턴의 시작 전으로
        i += 1
        j += 1
    if j == M:  # 패턴을 찾은 경우
        return i-M
    else:
        return -1

print(bf(p, t, N, M))


def bf2(p, t, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]: # 다르면 반복문 끝냄
                break
        else: # 같으면 i값 리턴
            return i
    return -1

print(bf2(p, t, N, M))

# 패턴이 여러개 있는 경우
def bf3(p, t, N, M):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]: # 다르면 반복문 끝냄
                break
        else:
            cnt += 1
    return cnt

print(bf3(p, t, N, M))

