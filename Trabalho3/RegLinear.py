import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

np.random.seed(1234)  # para reproducibilidade

# Carregar os dados
boston = load_boston()

print(boston.data.shape)
print(boston.target.shape)

# Embaralhar os dados
#  (como vamos dividir os dados em dois grupos a partir de um pivot,
#  este passo é necessario para caso os dados estejam ordenados por algum(ns) atributo(s))
p = np.random.permutation(len(boston.data))
boston.data, boston.target = boston.data[p], boston.target[p]

# Observando o dominio dos atributos de X:
print(np.max(boston.data, axis=0))

# Normalizar os dados de X para cada coluna, pois as colunas estao em escalas muito diferentes:
# A normalizazao usada (standardization)
# se faz subtraindo a media e dividindo pelo desvio padrao para cada coluna

boston.data = (boston.data - boston.data.mean(axis=0)) / boston.data.std(axis=0)

# Adicionando uma coluna de 1's ao X:
boston.data = np.concatenate([np.ones(shape=[len(boston.data), 1]), boston.data], axis=1)

print("Novas dimensoes do X:", boston.data.shape)

# Definir quantos % do dataset será usado para treino
train_size = 0.8  # 80% para treino e 20% para teste
train_cut_point = int(train_size * len(boston.data))

X_train = boston.data[:train_cut_point]
y_train = boston.target[:train_cut_point]

X_test = boston.data[train_cut_point:]
y_test = boston.target[train_cut_point:]

print("Dataset de treino:", X_train.shape, y_train.shape)
print("Dataset de teste:", X_test.shape, y_test.shape)

alpha = 0.01  # taxa de aprendizado (learning rate)
n_epochs = 1000  # quantidade de passos de treinamento

# Pesos iniciais w aleatorios:
w = np.random.uniform(size=X_train.shape[1])

# Fase de treinamento:
for epoch in range(n_epochs):

    predicted_yi_list = []
    error_list = []

    grads = np.zeros(shape=w.shape)

    # Para cada exemplo:
    for i in range(len(X_train)):
        predicted_yi = np.dot(w, X_train[i])

        predicted_yi_list.append(predicted_yi)

        e_i = y_train[i] - predicted_yi

        grads = grads + e_i * X_train[i]

    # Etapa de atualizacao dos parametros:
    w = w + (alpha * (1 / len(X_train)) * grads)

    # Mostrando o erro medio quadratico para cada epoca:
    print("Epoca: {} - {}".format(epoch, mean_squared_error(y_train, predicted_yi_list)))

# Calculando algumas metricas para medir o desempenho do modelo para os dados de treino
# (erro medio absoluto e erro medio quadratico)
train_mean_squared_error = mean_squared_error(y_train, predicted_yi_list)
train_mean_absolute_error = mean_absolute_error(y_train, predicted_yi_list)

print("Erro medio\n  Quadratico: {}\n  Absoluto: {}".format(train_mean_squared_error, train_mean_absolute_error))
plt.figure(figsize=(10,6))
plt.plot(y_train, predicted_yi_list, "x")
plt.plot([min(y_train),max(y_train)], [min(y_train),max(y_train)], "r")
plt.title("Dataset de Treino")
plt.show()

# Testando o modelo para o conjunto de teste:
predicted_yi_list = []
for i in range(len(X_test)):
    predicted_yi = np.dot(w, X_test[i])

    predicted_yi_list.append(predicted_yi)

# Calculando algumas metricas para medir o desempenho do modelo para os dados de teste
# (erro medio absoluto e erro medio quadratico)
test_mean_squared_error = mean_squared_error(y_test, predicted_yi_list)
test_mean_absolute_error = mean_absolute_error(y_test, predicted_yi_list)

print("Erro medio\n  Quadratico: {}\n  Absoluto: {}".format(test_mean_squared_error, test_mean_absolute_error))

plt.figure(figsize=(10,6))
plt.plot(y_test, predicted_yi_list, "x")
plt.plot([min(y_test),max(y_test)], [min(y_test),max(y_test)], "r")
plt.title("Dataset de Teste")
plt.show()
