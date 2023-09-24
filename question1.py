def encontre_R_e_S(pares):
    # Inicialize R* como -infinito e S* como um conjunto vazio
    R_star = float('-inf')
    S_star = set()

    # Itere sobre cada par (a, b) no conjunto de pares
    for a, b in pares:
        # Calcule a razão R para o par (a, b)
        R = a / b

        # Se a razão R for maior que R*, atualize R* e redefina S* como {a, b}
        if R > R_star:
            R_star = R
            S_star = {(a, b)}

        # Se a razão R for igual a R*, adicione o par (a, b) a S*
        elif R == R_star:
            S_star.add((a, b))

    return R_star, S_star

# Exemplo de uso
pares = []
for i in range(1, 6):
    for j in range(1,6):
        pares.append((i, j))
    
print(pares)
R_maximo, S_maximo = encontre_R_e_S(pares)

print("R* (Razao Maxima):", R_maximo)
print("S* (Conjunto de Pares Correspondentes):", S_maximo)
