# key를 입력받아 nums의 idx를 return
def find(key):
    # while문 쓰는 경우
    idx = 0
    while idx < N and nums[idx] < key:
        idx += 1
    if idx < N and nums[idx] == key:
        return idx
    else:
        return -1
    # for문 쓰는 경우
    # for idx in range(7):
    #     if nums[idx] == key:
    #         return idx
    # return -1

# def find(key):
#     i = 0
#     while i < N and nums[i] < key:
#         i += 1
#     if i < N and nums[i] == key:  # 검색 성공한 경우
#         return i
#     else:
#         return -1  # key값 없어 검색 실패한 경우


N = 7
nums = [2, 4, 7, 9, 11, 19, 23]
#nums = [4, 9, 11, 23, 2, 19, 7]

print(find(4)) #0
print(find(19)) #5
print(find(7)) #6
print(find(1)) #-1


