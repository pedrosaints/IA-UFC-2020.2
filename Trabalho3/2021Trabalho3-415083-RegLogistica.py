import numpy as np
import matplotlib.pyplot as plt
print("---------- TRABALHO 3 ----------")
print()
print("----- VALORES DO PROBLEMA -----")

# X = [0,1,2,3,4,1.2,0.5,2.6,2.3,2.4,2.1,1.6,1.4]
# Y = [1,2,2,1,2,1,1,1,1,2,2,2,2]

X = [
[0,1.5],
[1,2.1],
[2,2.6],
[3,1.6],
[4,2.4],
[1.2,2.3],
[3.5,1.4],
[4,2.7],
[4,1.1],
[2,1.3],
     ]
print("X:")
print(X)

X = np.concatenate([np.ones(shape=[len(X), 1]), X], axis=1)
print("X:")
print(X)

Y = [0,1,1,0,1,1,0,1,0,0]
print("Y:")
print(Y)

W0 = [1,1,1]
print("W0:")
print(W0)

def calcula_erro(X,Y,W):
    erro = Y
    for j in range(len(W)):
        Xi = np.copy(X)
        erro -= 1/(1+np.exp(-W[j] * Xi[j]))
    print(erro)
    return erro

def calcula_logistica(X,Y,W):
    result = 0
    for j in range(len(W)):
        result += 1/(1+(np.exp(-W[j] * X[j])))
    print(result)
    return result

def calcula_som(X,Y,W):
    soma = np.zeros(len(W))
    for i in range(len(Y)):
        Xi = np.copy(X[i])
        # ERRO AQUI
        soma += calcula_erro(Xi,Y[i],W) * calcula_logistica(Xi,Y[i],W) * calcula_erro(Xi,1,W) * Xi
        #          Y - H(X)                       H(X)                         1 - H(X)
        print()
    return soma

def calcula_peso(X,Y,W):
    Wi = np.copy(W)
    # 0.1 é a constante que define o tamanho do passo na derivada
    C = 0.1/len(X)
    return (Wi + (C*calcula_som(X,Y,W)))

def calcula_coef(X,Y,W):
    print()
    print("----- CALCULANDO COEFICIENTES -----")
    Wi = np.copy(W)
    Wf = calcula_peso(X,Y,Wi)
    print(Wf)
    # erro = calcula_erro(X[0],Y[0],Wi) - calcula_erro(X[0],Y[0],Wf)
    # while(erro > 0.01):
    #     print("Ybarra atual:")
    #     print(calcula_y(X, Wf))
    #     Wi = Wf
    #     Wf = calcula_peso(X, Y, Wi)
    #     erro = calcula_erro(X[0], Y[0], Wi) - calcula_erro(X[0], Y[0], Wf)
    return Wf

def calcula_y(X,W):
    Y = np.zeros(len(X))
    for i in range(len(Y)):
        Y[i] = 0
        for j in range(len(W)):
            Y[i] += X[i][j] * W[j]
    return Y

print(calcula_y(X,W0))

W = calcula_coef(X,Y,W0)
print()
print()
print("* COEFICIENTES CALCULADOS:")
print(W)
print()
print("* EQUACAO:")
print("Y =",W[0]," + X1 *",W[1]," + X2 *",W[2])
print()
print("* YBARRA FINAL:")
print(calcula_y(X,W))



# plt.figure(figsize=(10,6))
# plt.plot(Xg, Yg, "x")
# plt.title("Dataset de Treino")
# plt.show()