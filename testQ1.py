import random


def primeiro_algoritmo(a, b):
    n = len(a)
    S = []
    R = a[0] / b[0]
    for i in range(1, n):
        if a[i] / b[i] > R:
            S.append((a[i], b[i]))
            R = a[i] / b[i]
            j = len(S) - 1
            while j > 0 and S[j][0] / S[j][1] > S[j-1][0] / S[j-1][1]:
                S[j], S[j-1] = S[j-1], S[j]
                j -= 1
            while j < len(S) - 1 and S[j][0] / S[j][1] < S[j+1][0] / S[j+1][1]:
                S[j], S[j+1] = S[j+1], S[j]
                j += 1
            while len(S) > 0 and S[0][0] / S[0][1] < R:
                S.pop(0)
    return R, S


n = 50  # tamanho das listas
a = [random.randint(1, 10) for _ in range(n)]
b = [random.randint(1, 10) for _ in range(n)]

print("a =", a)
print("b =", b)

R, S = primeiro_algoritmo(a, b)

print("R =", R)
print("S =", S)
