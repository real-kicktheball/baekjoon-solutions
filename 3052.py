list1 = []
for _ in range(10):
    num = int(input()) % 42
    if num in list1:
        continue
    list1.append(num)

print(len(list1))
