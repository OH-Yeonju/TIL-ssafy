s = '444345'
l = list(map(int, s))

# l = list(map(int, input()))
print(l)

counts = [0] * 12  # 한자릿수기때문에, + 뒤에 두칸 그냥 넣어주기..
for num in l:
    counts[num] += 1

print(counts)

tri = 0
run = 0
i = 0
while i < 10:
    if counts[i] >= 3:
        counts[i] -= 3
        tri += 1
        continue
    if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue
    i += 1

print(tri, run)