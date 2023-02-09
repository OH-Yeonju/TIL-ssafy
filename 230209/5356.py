T = int(input())

for tc in range(1, T + 1):
    word = [list(input()) for _ in range(5)]
    new_word = [] # 답 리스트 생성

    minLen = 16
    maxLen = 0
    for i in word: # 각 줄의 길이 최소, 최대값 구함
        wLen = len(i)
        if minLen > wLen:
            minLen = wLen
        if maxLen < wLen:
            maxLen = wLen

    for i in range(minLen): # 최소값까지는 모두가 요소 있음. 반복문 돌리기 가능
        for j in range(5):
            new_word.append(word[j][i])

    for i in range(minLen, maxLen): # 최소값 이상일 시 없는 줄이 존재, 각 줄에서 요소 뽑아서 각각 넣어줌
        for j in word:
            if len(j) > i:
                new_word.append(j[i])

    print(f'#{tc}',' ', *new_word, sep='')



    # print(f'{tc}', *new_word)