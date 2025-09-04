import random

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, node, valor):
        if valor < node.valor:
            if node.esquerda is None:
                node.esquerda = Node(valor)
            else:
                self._inserir(node.esquerda, valor)
        else:
            if node.direita is None:
                node.direita = Node(valor)
            else:
                self._inserir(node.direita, valor)

    def inorder(self):
        return self._inorder(self.raiz)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.esquerda) + [node.valor] + self._inorder(node.direita)

    def preorder(self):
        return self._preorder(self.raiz)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.valor] + self._preorder(node.esquerda) + self._preorder(node.direita)

    def postorder(self):
        return self._postorder(self.raiz)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.esquerda) + self._postorder(node.direita) + [node.valor]

    def visualizar(self):
        # Visualização simples em texto (rotacionada 90 graus)
        def _visualizar(node, prefixo="", is_left=True):
            if node is not None:
                _visualizar(node.direita, prefixo + ("│   " if is_left else "    "), False)
                print(prefixo + ("└── " if is_left else "┌── ") + str(node.valor))
                _visualizar(node.esquerda, prefixo + ("    " if is_left else "│   "), True)
        _visualizar(self.raiz)

# Árvore com valores fixos
valores_fixos = [55, 30, 80, 20, 45, 70, 90]
arvore_fixa = ArvoreBinaria()
for v in valores_fixos:
    arvore_fixa.inserir(v)

print("Árvore Binária com valores fixos:")
arvore_fixa.visualizar()
print("In-Order:", arvore_fixa.inorder())
print("Pre-Order:", arvore_fixa.preorder())
print("Post-Order:", arvore_fixa.postorder())
print("\n" + "="*40 + "\n")

# Árvore com valores randômicos
valores_random = random.sample(range(10, 100), 10)
arvore_random = ArvoreBinaria()
for v in valores_random:
    arvore_random.inserir(v)

print("Árvore Binária com valores randômicos:", valores_random)
arvore_random.visualizar()
print("In-Order:", arvore_random.inorder())
print("Pre-Order:", arvore_random.preorder())
print("Post-Order:", arvore_random.postorder())
