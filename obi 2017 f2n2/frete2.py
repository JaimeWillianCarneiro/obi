def different_sums(arr):
    memo = {}  # Dicionário para armazenar os resultados intermediários

    def dp(start):
        if start >= len(arr):
            return {0}  # Caso base: conjunto vazio com a soma 0
        if start in memo:
            return memo[start]

        # Chamada recursiva considerando o elemento atual ou não
        with_current = {arr[start] + s for s in dp(start + 1)}
        without_current = dp(start + 1)

        # Armazena o resultado no dicionário (união dos conjuntos)
        memo[start] = with_current.union(without_current)

        return memo[start]

    return dp(0)

# Exemplo de uso:
lista = [1, 2, 3]
somas_diferentes = different_sums(lista)
print(somas_diferentes)
