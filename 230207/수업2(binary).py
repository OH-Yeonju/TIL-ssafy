def find(key):
    s = 0
    e = N-1
    while s <= e:
        m = (s+e)//2
        if nums[m] == key:
            return m
        if nums[m] < key:
            s = m+1
        else:
            e = m-1
    return -1

nums = [2, 4, 7, 9, 11, 19, 23]
N = 7
print(find(9))