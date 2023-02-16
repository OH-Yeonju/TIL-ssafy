# # 거듭제곱
# def power(Base, Exponent):
#     if Base == 0:
#         return 1
#     result = 1
#     for i in range(Exponent):
#         result *= Base
#     return result




def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)