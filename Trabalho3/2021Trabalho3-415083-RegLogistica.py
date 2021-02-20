import numpy as np
import csv

with open("data.data") as data:
    content = data.read().splitlines()
    y = np.zeros(len(content))
    x = np.zeros((len(content),len(content[0].split(","))-2))
    for i in range(len(content)):
        linhacontent = content[i].split(",")
        # B = 0, M = 1
        if linhacontent[1] == "B":
            y[i] = 0
        else:
            y[i] = 1
        for j in range(2,len(linhacontent)):
            x[i][j-2] = linhacontent[j]


    print("---------- TRABALHO 3 ----------")
    print()
    print("----- VALORES DO PROBLEMA -----")

    # 0.001 é a constante que define o tamanho do passo na derivada
    C = 0.001
    EPOCAS = 100000

    # print("X:")
    # print(x)
    x = x.reshape(-1, 1) if len(x.shape) < 2 else x
    x = np.insert(x, 0, 1, 1)
    # print(x)

    # print("Y:")
    # print(y)

    w0 = np.random.normal(0, 1, size=x[0].shape)
    print("W0:")
    print(w0)

    def calcula_logistica(X,W):
        result = 1 / (1 + np.exp(-np.dot(X, W)))
        # print(result)
        return result

    def calcula_som(X,Y,W):
        soma = np.zeros(len(W))
        for i in range(len(Y)):
            Xi = np.copy(X[i])
            # VER AQUI
            soma += np.dot(calcula_logistica(Xi,W) - Y[i], Xi)
        return soma

    def calcula_peso(X,Y,W):
        Wi = np.copy(W)
        return (Wi - (C*calcula_som(X,Y,W)))

    def calcula_coef(X,Y,W):
        print()
        print("----- CALCULANDO COEFICIENTES -----")
        Wi = np.copy(W)
        Wf = calcula_peso(X,Y,Wi)
        # print(Wf)
        for _ in range(EPOCAS):
            # print("Ybarra atual:")
            # print(calcula_y(X, Wf))
            Wi = Wf
            Wf = calcula_peso(X, Y, Wi)
        return Wf

    def calcula_y(X,W):
        Y = np.dot(X, W)
        for i in range(len(Y)):
            if Y[i] > 0:
                Y[i] = 1
            else:
                Y[i] = 0
        return Y


    print()
    # print("Y inicial")
    # print(calcula_y(x,w0))

    W = calcula_coef(x,y,w0)
    print()
    print()
    print("* COEFICIENTES CALCULADOS:")
    print(W)
    print()
    print("* EQUACAO:")
    eq = "Y =" + str(W[0])
    for i in range(len(w0)):
        eq += " + X" + str(i) + "*" + str(W[i])
    print(eq)
    print()
    print("* YBARRA FINAL:")
    yf = calcula_y(x,W)
    print(yf)

    print('Porcentagem de acerto: ', np.mean(np.equal(yf, y)))





