def partial(k, curS, key):
    # if curS > 10:
    #     return
    if k == N:
        print(bits, curS)
        if curS == key:
            return 1
        return 0

    bits[k] = 0
    if partial(k+1, curS, key):
        return 1
    bits[k] = 1
    if partial(k+1, curS+nums[k], key):
        return 1

    return 0

nums = [1, 2, 3, 4, 5]
N = 5
bits = [-1] * N
key = 100
print(partial(0, 0, key))
