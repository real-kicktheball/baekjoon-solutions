n = 1
for i in range(3):
    x = int(input())
    n *= x
n_list = [int(i) for i in str(n)]
for i in range(10):
    print(n_list.count(i))
