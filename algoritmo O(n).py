def encontrar_S_estrela(pares):
    R_max = float("-inf")
    S_estrela = []

    for i, (a, b) in enumerate(pares):
        R_i = a / b

        if R_i > R_max:
            R_max = R_i
            S_estrela = [i]
        elif R_i == R_max:
            S_estrela.append(i)

    return S_estrela, R_max

# Exemplo de uso com pares ordenados (ai, bi)
pares_ordenados = [(3, 2), (4, 3), (2, 1), (5, 4)]
S_estrela, R_max = encontrar_S_estrela(pares_ordenados)

print("Conjunto S*: ", S_estrela)
print("Valor maximo da razao R(S*): ", R_max)
