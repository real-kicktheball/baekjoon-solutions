N, X = map(int, input().split())
list1 = []
for i in map(int, input().split()):
    if i < X:
        list1.append(i)
print(*list1)
