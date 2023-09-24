import random

def encontrar_R_e_S(pares, a0, b0):
    n = len(pares)
    R = a0 / b0
    S = {0}  # Começa com o par obrigatório (a0, b0)

    for i in range(1, n):
        ai, bi = pares[i]
        if ai / bi > R:
            S.add(i)
            R = sum(pares[j][0] for j in S) / sum(pares[j][1] for j in S)

        # Remove elementos de S que não satisfazem o lema
        S.difference_update(j for j in S if pares[j][0] / pares[j][1] <= R)

    return R, S

# Exemplo de uso


# Gerar pares ordenados aleatórios
n = 10  # Número de pares
pares = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(n)]

# Par obrigatório (a0, b0)
a0, b0 = random.choice(pares)

R, S = encontrar_R_e_S(pares, a0, b0)

print("R+:", R)  # Imprime o valor de R+
print("S*:", S)  # Imprime o conjunto S* que maximiza R+
