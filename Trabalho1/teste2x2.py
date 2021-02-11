import numpy as np
import math


def produzSolucao():
    S = np.zeros((n, n))
    C = 0
    for i in range(n):
        for j in range(n):
            C += 1
            S[i][j] = C
    S[n - 1][n - 1] = 0
    return S


# TAMANHO DO TABULEIRO
n = 2
Sol = produzSolucao()
MAXIMO = math.factorial(n * n)
print(MAXIMO)


class NodoArvore:
    def __init__(self, chave=None, origem="", pai=None, altura=0, filhos=None):
        self.chave = chave
        self.origem = origem
        self.pai = pai
        self.filhos = filhos
        self.altura = altura

    def __repr__(self):
        return '\n%s\n%s\n' % (self.chave[0], self.chave[1])


def buscaArv(no, movAnterior):
    if no.altura < MAXIMO:
        estados = []
        i, j, mov = verificaMovimentacao(no.chave)
        for k in range(len(mov)):
            S = np.copy(no.chave)
            if (verificaSolucao(Sol, S) == False):
                if mov[k] == "U" and movAnterior != "D":
                    S[i][j] = S[i - 1][j]
                    S[i - 1][j] = 0
                    filho = NodoArvore(S, mov[k], no, no.altura + 1)
                    estados.append(filho)
                if mov[k] == "D" and movAnterior != "U":
                    S[i][j] = S[i + 1][j]
                    S[i + 1][j] = 0
                    filho = NodoArvore(S, mov[k], no, no.altura + 1)
                    estados.append(filho)
                if mov[k] == "L" and movAnterior != "R":
                    S[i][j] = S[i][j - 1]
                    S[i][j - 1] = 0
                    filho = NodoArvore(S, mov[k], no, no.altura + 1)
                    estados.append(filho)
                if mov[k] == "R" and movAnterior != "L":
                    S[i][j] = S[i][j + 1]
                    S[i][j + 1] = 0
                    filho = NodoArvore(S, mov[k], no, no.altura + 1)
                    estados.append(filho)

        no.filhos = estados
        # print(estados)
        for e in no.filhos:
            buscaArv(e, e.origem)


def caminho(no):
    if no.pai:
        caminho(no.pai)
        print(no)


def solucao(no):
    if not no:
        return
    if not no.filhos:
        # folha
        print()
        if verificaSolucao(Sol, no.chave):
            print("SOLUCAO:")
            caminho(no)
            print()
    elif len(no.filhos) > 0:
        for e in no.filhos:
            solucao(e)


def produzEstado():
    S = np.arange(n * n)
    np.random.shuffle(S)
    return S.reshape((n, n))


def produzPopulacao(Tam):
    P = []
    for i in range(Tam):
        P.append(produzEstado())
    return P


def verificaMovimentacao(S):
    M = []
    # U: up
    # D: down
    # L: left
    # R: right
    i, j = np.where(S == 0)
    # print(i)
    if i != 0:
        M.append("U")
    if i != (n - 1):
        M.append("D")
    if j != 0:
        M.append("L")
    if j != (n - 1):
        M.append("R")

    # print(M)
    return i[0], j[0], M


def verificaSolucao(Sol, S):
    A = Sol - S
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                # print("Cont")
                return False
    # print("OK")
    return True


Sa = produzEstado()
P = produzPopulacao(10)
# for i in range(len(P)):
# print(P[i])

raiz = NodoArvore(Sa)
print("PARA A ENTRADA:")
print(raiz)
buscaArv(raiz, "")
solucao(raiz)