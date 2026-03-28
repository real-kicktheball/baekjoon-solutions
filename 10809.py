import string

S = input()

alphabet = string.ascii_lowercase

result = []
for char in alphabet:
    result.append(str(S.find(char)))

print(" ".join(result))
