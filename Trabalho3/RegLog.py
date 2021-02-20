import numpy as np
from matplotlib import pyplot as plt, style
from IPython import display

style.use('ggplot')
np.random.seed(2)

x = np.linspace(15,42,15).astype(int)
y_logit = x*-0.5 + 15 + np.random.normal(0,1.5, x.shape)
y = np.round(np.exp(y_logit) / (np.exp(y_logit) + 1), 0)

plt.scatter(x, y)
plt.show()



# from sklearn.linear_model import LinearRegression
# regr = LinearRegression()
# regr.fit(x.reshape(-1,1), y)
# line = regr.predict(x.reshape(-1,1))
#
# plt.scatter(x, y)
# plt.plot(x, line, c='C1')
# plt.axvline(x=(0.5 - regr.intercept_)/regr.coef_, c='k', ls='dotted', lw=1)
# plt.show()





# x_ = np.array([[100]])
# y_ =  x_*-0.5 + 15 + np.random.normal(0,1.5, 1)
# y_ = np.round(np.exp(y_) / (np.exp(y_) + 1), 0)
#
# x = np.append(x, x_)
# y = np.append(y, y_)
#
# regr = LinearRegression()
# regr.fit(x.reshape(-1,1), y)
# line = regr.predict(x.reshape(-1,1))
#
# plt.scatter(x, y)
# plt.plot(x, line, c='C1')
# plt.axvline(x=(0.5 - regr.intercept_)/regr.coef_, c='k', ls='dotted', lw=1)
# plt.show()




# from sklearn.linear_model import LogisticRegression
#
# clf = LogisticRegression(C=1e7)
# clf.fit(x.reshape(-1,1), y)
#
# def model(x):
#     return 1 / (1 + np.exp(-x))
#
# line = np.linspace(1, 110, 500)
# line = model(line * clf.coef_ + clf.intercept_).ravel()
#
# plt.scatter(x, y)
# plt.plot(np.linspace(1, 110, 500), line, c='C1')
# plt.axvline(x=0.5 - (clf.intercept_/clf.coef_), c='k', ls='dotted', lw=1)
# plt.show()
#
# print('Acurácia: %.3f' % clf.score(x.reshape(-1,1), y))
# print('Os parâmetros do modelos são: %.3f, %.3f' % (clf.intercept_, clf.coef_))



# def sigmoid(x):
#     return 1/(1 + np.exp(-x))
# plt.plot(np.linspace(-10,10,100), sigmoid(np.linspace(-10,10,100)), lw=5)
# plt.show()


class logistic_regr(object):

    def __init__(self, learning_rate=0.0001, training_iters=100):
        self.learning_rate = learning_rate  # taxa de aprendizado
        self.training_iters = training_iters  # iterações de treino

    def _logistic(self, X):
        '''Função logística'''
        return 1 / (1 + np.exp(-np.dot(X, self.w_hat)))

    def fit(self, X_train, y_train):

        # formata os dados
        X = X_train.reshape(-1, 1) if len(X_train.shape) < 2 else X_train
        X = np.insert(X, 0, 1, 1)

        # inicia os parâmetros com pequenos valores aleatórios (nosso chute razoável)
        self.w_hat = np.random.normal(0, 1, size=X[0].shape)

        # loop de treinamento
        for _ in range(self.training_iters):

            gradient = np.zeros(self.w_hat.shape)  # inicia o gradiente

            # atualiza o gradiente com informação de todos os pontos
            for var in range(len(gradient)):
                gradient[var] += np.dot((self._logistic(X) - y_train), X[:, var])

            gradient *= self.learning_rate  # multiplica o gradiente pela taxa de aprendizado

            # atualiza os parâmetros
            self.w_hat -= gradient

    def predict(self, X_test):

        # formata os dados
        if len(X_test.shape) < 2:
            X = X_test.reshape(-1, 1)
        X = np.insert(X, 0, 1, 1)

        # aplica função logística
        logit = self._logistic(X)

        # aplica limiar
        return np.greater_equal(logit, 0.5).astype(int)


regr = logistic_regr(learning_rate=0.001, training_iters=90000)
regr.fit(x, y)
y_hat = regr.predict(x)
print('Acurácia: ', np.mean(np.equal(y_hat, y)))
print('Os parâmetros do modelos são: %.3f, %.3f' % (regr.w_hat[0], regr.w_hat[1]))

print(np.ones(shape=[len(x), 1]))
print(x)
print(y)
result = []
for i in range(len(x)):
    r = regr.w_hat[0]*1 + regr.w_hat[1] * x[i]
    if r > 0:
        result.append(1)
    else:
        result.append(0)
print(result)

# def model(x):
#     return 1 / (1 + np.exp(-x))
#
# line = np.linspace(1, 110, 500)
# line = model(line * regr.w_hat[1] + regr.w_hat[0).ravel()
#
# plt.scatter(x, y)
# plt.plot(np.linspace(1, 110, 500), line, c='C1')
# plt.axvline(x=0.5 - (regr.w_hat[0]/regr.w_hat[1]), c='k', ls='dotted', lw=1)
# plt.show()

# print('Acurácia: %.3f' % clf.score(x.reshape(-1,1), y))
# print('Os parâmetros do modelos são: %.3f, %.3f' % (clf.intercept_, clf.coef_))