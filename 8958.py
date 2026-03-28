for _ in range(int(input())):
    score = 1
    total = 0
    quiz = str(input())
    for i in quiz:
        if i == "O":
            total += score
            score += 1
        else:
            score = 1
    print(total)
