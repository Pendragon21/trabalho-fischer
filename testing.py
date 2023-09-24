def maximize_R(pairs, a0, b0):
    n = len(pairs)
    DP = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-1] * (a0 + sum(pairs[i-1][0] for k in S) / (b0 + sum(pairs[i-1][1] for k in S))))

    S = []
    i, j = n, n
    while i > 0 and j > 0:
        if DP[i][j] != DP[i-1][j]:
            S.append(i)
            j -= 1
        i -= 1

    return S

# Exemplo de uso:
pairs = [(1, 2), (3, 4), (5, 6), ...]  # Lista de pares ordenados
a0, b0 = 1, 2  # Par obrigatório
S = maximize_R(pairs, a0, b0)
print("Conjunto S que maximiza R(S):", S)
