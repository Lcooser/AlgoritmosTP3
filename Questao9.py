# Estrutura da árvore binária
# Cada nó tem um valor e dois filhos: esquerda e direita
class No:
    def __init__(self, valor):
        self.valor = valor 
        self.esquerda = None 
        self.direita = None 

# Função recursiva para percorrer a árvore em ordem
# A ordem é: subárvore esquerda, nó atual, subárvore direita
def percorrer_em_ordem(no, resultado=None):
    if resultado is None:
        resultado = []  # Inicializa a lista de resultados

    # Caso base: se o nó for None, não faz nada
    if no is not None:
        # Primeiramente, percorre a subárvore esquerda
        percorrer_em_ordem(no.esquerda, resultado)
        # Depois, adiciona o valor do nó atual à lista de resultados
        resultado.append(no.valor)
        # Finalmente, percorre a subárvore direita
        percorrer_em_ordem(no.direita, resultado)

    return resultado

# Exemplo de árvore binária
# Criando uma árvore binária com a seguinte estrutura:
#       10
#      /  \
#     5   15
#    / \   / \
#   3  7  12  18
raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)
raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)
raiz.direita.esquerda = No(12)
raiz.direita.direita = No(18)

# Chamando a função de percorrimento e armazenando o resultado
resultado = percorrer_em_ordem(raiz)

# Exibindo o resultado: valores dos nós em ordem
print("Valores dos nós em ordem:", resultado)
