n = int(input())

for i in range(n+1, 1, -1):
    for j in range(i-2):
        print(" ", end="")
    for k in range(n+2-i):
        print("*", end="")
    print("")
