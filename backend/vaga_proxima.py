vagas = [
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 1, 1],
]

def encontrar_vaga_mais_proxima():
    for i, row in enumerate(vagas):
        for j, vaga in enumerate(row):
            if vaga == 0:  # Vaga disponível
                return i, j
    return None

vaga_proxima = encontrar_vaga_mais_proxima()
print(f"Vaga mais próxima: {vaga_proxima}")
