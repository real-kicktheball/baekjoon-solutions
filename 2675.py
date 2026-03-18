for i in range(int(input())):
    a, b = map(str, input().split())
    for j in str(b):
        print(j * int(a), end = "")
    print()
        
