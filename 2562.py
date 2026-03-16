num_list = [0 for i in range(9)]
for i in range(9):
    num_list[i] = int(input())
print(max(num_list), num_list.index(max(num_list))+1)
